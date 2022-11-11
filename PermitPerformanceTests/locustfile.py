from locust import HttpUser, task
import json


def load_file(file_name: str):
    with open(file=file_name, mode="r") as open_file:
        output = json.load(open_file)
    return output


class PermitApp(HttpUser):
    env_name = "Env2_Permits_PL_Dev"
    host_name = "identitydev.xrxpsc.com"

    @task
    def vehicle_lookup(self):
        self.client.get(f"/{self.env_name}/lookupvehicle/T2OMF")
        self.client.get(f"/{self.env_name}/lookupcharge/T2OMF")
        self.client.get(f"/{self.env_name}/lookupdiscount/T2OMF")

    @task
    def paid_permits(self):
        self.client.get(
            f"/{self.env_name}/getpaidpermits/f32fb0e0-3648-46e4-f424-08da10a5c396")

    @task
    def start_payment(self):
        self.client.post(url=f"{self.env_name}/startpayment",
                         json=load_file("json/start_payment.json"),
                         headers={"referer": f"https://{self.host_name}/{self.env_name}/Checkout",
                                  "Content-Type": "application/json"})
