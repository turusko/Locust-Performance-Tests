import json
import requests
import enviroment_loader


def save_new_auth_token():

    response = requests.post(url=enviroment_loader.get_environment_value("authUrl"),
                             headers={"Content-Type": "application/json"},
                             json={
                                 "userName": enviroment_loader.get_environment_value("UserName"),
                                 "password": enviroment_loader.get_environment_value("Password")
                             })
    with open("auth.json", "w") as open_file:
        json.dump(response.json(), open_file)
