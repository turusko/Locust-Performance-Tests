from time import sleep
import enviroment_loader
import locust
from locust.exception import RescheduleTask
from static_data import get_media_file
import logging
from ..models import CCTVMediaConfig
from ..payloads import get_payload_new_case

application_settings = enviroment_loader.load_application_settings()

class SiteWebUpload(locust.SequentialTaskSet):
    headers = {
        'Authorization': f'Bearer {enviroment_loader.get_auth_token()}',
        'Content-Type': 'application/json'
    }
    array = []
    last_notice_number = ''
    new_case = False

    @locust.task
    def post_new_case(self):
        url = "/v2/Case/Upload"
        with self.client.post(url, headers=self.headers, json=get_payload_new_case(), catch_response=True) as response:
            if response.status_code == 200 or response.status_code == 201:
                response.success()
                self.array.append(response.json()["toolKitNoticeNumber"])
                self.last_notice_number = response.json()["toolKitNoticeNumber"]
                self.new_case = True
                logging.info(f'Task: post_new_case, status code = {response.status_code}, content= {response.content}')
            else:
                self.new_case = False
                logging.error(f'Task: post_new_case, status code = {response.status_code}, content= {response.content}')
                raise RescheduleTask()

    @locust.task
    def post_media_photo(self):
        url = "/v2/media/Upload"
        if self.new_case:
            with self.client.post(url, headers=self.headers,
                                  data=CCTVMediaConfig(get_media_file().strip(), "jpg", self.last_notice_number, False).to_json(),
                                  catch_response=True) as response:
                if response.status_code == 200 or response.status_code == 201:
                    response.success()
                    logging.info(
                        f'Task: post_media_photo, status code = {response.status_code}, content= {response.content}')
                else:
                    logging.error(
                        f'Task: post_media_photo, status code = {response.status_code}, content= {response.content}')
                    raise RescheduleTask()

    @locust.task
    def put_complete_case(self):
        if len(self.array) >= application_settings.max_cases:
            sleep(application_settings.max_wait)
            for i in list(self.array):
                url = "/v2/case/Complete/" + str(i)
                logging.info(url)
                with self.client.put(url=url, headers={
                    'Authorization': f'Bearer {enviroment_loader.get_auth_token()}'}) as response:
                    if response.status_code == 200 or response.status_code == 201 or response.status_code == 204:
                        response.success()
                        logging.info(
                            f'Task: put_complete_case, status code = {response.status_code}, content= {response.content}')
                        self.array.remove(i)
                    else:
                        logging.error(
                            f'Task: put_complete_case, status code = {response.status_code}, content= {response.content}')
    @locust.task
    def end(self):
        if len(self.array) >= application_settings.max_cases:
            self.user.environment.reached_end = True
            self.user.environment.runner.quit()

                            
