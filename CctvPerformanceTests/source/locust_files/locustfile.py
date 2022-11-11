from locust import HttpUser, task, between
import common

class MyUser(HttpUser):
    tasks = [common.SiteWebUpload]
