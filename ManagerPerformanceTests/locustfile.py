from __future__ import annotations
from locust import HttpUser, TaskSet, task, between
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import Optional
from datetime import datetime

import requests

# Supress SSl warnings
requests.packages.urllib3.disable_warnings()

# Constants for config
TENANT_ID = '0A5A4117-7009-43C4-B165-2A12B6C82298'
ENFORCEMENT_CODE = 'LEZ'
CAMERA_SERIAL_NUMBER = 'lezcamref001'
CAMERA_REFERENCE_NUMBER = 'lezcam001'


# Data Models
@dataclass_json
@dataclass
class Config:
    hostname: Optional['str']
    auth: Optional['str']
    auth_type: Optional['str']
    verify_ssl: bool


@dataclass_json
@dataclass
class PermitCheckPayload:
    tenantId: str
    vrm: str
    eventDate: str
    enforcementCode: str
    cameraSerialNumber: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    cameraReferenceNumber: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    autoCreateUnpaidPermit: Optional[bool] = field(default=None, metadata=config(exclude=lambda f: f is None))


@dataclass_json
@dataclass
class ExemptionsCheckPayload:
    tenantId: str
    enforcementCode: str
    vrm: str
    eventDateTime: str
    cameraSerialNumber: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    cameraReferenceNumber: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    includeVehicleLookup: Optional[bool] = field(default=None, metadata=config(exclude=lambda f: f is None))
    includePermit: Optional[bool] = field(default=None, metadata=config(exclude=lambda f: f is None))
    includeCharge: Optional[bool] = field(default=None, metadata=config(exclude=lambda f: f is None))
    includeDiscount: Optional[bool] = field(default=None, metadata=config(exclude=lambda f: f is None))


# Open config
with open("config.json") as open_file:
    FILE_DATA = open_file.read()
CONFIG_SET = Config.from_json(FILE_DATA)


# Locust Task Sets
class PermitCheck(TaskSet):
    headers = {
        'Authorization': f'{CONFIG_SET.auth_type} {CONFIG_SET.auth}',
        'Content-Type': 'application/json'
    }

    @task
    def lookup_vehicle(self):
        payload = PermitCheckPayload(
            '0A5A4117-7009-43C4-B165-2A12B6C82298',
            'T20mf',
            '2022-05-23T13:00:48.420Z',
            'LEZ',
            'lezcamref001',
            'lezcam001',
            False
        )

        with self.client.post('PermitCheck',
                              headers=self.headers,
                              data=payload.to_json(),
                              verify=CONFIG_SET.verify_ssl,
                              catch_response=True) as response:
            if not response.status_code == 200:
                response.failure(f'Status code was not 200 but {response.status_code}')


class Exemptions(TaskSet):
    headers = {
        'Authorization': f'{CONFIG_SET.auth_type} {CONFIG_SET.auth}',
        'Content-Type': 'application/json'
    }

    @task
    def check(self):
        payload = ExemptionsCheckPayload(
            tenantId=TENANT_ID,
            enforcementCode=ENFORCEMENT_CODE,
            cameraReferenceNumber=CAMERA_REFERENCE_NUMBER,
            vrm='t2omf',
            eventDateTime=str(datetime.now().isoformat()),

        )
        with self.client.post('v2/exemptions/check',
                              headers=self.headers,
                              data=payload.to_json(),
                              verify=CONFIG_SET.verify_ssl,
                              catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f'Status code was not 200 but {response.status_code}, {response.content}')


# Locust Clients
class Runner(HttpUser):
    wait_time = between(1,5)
    host = CONFIG_SET.hostname
    tasks = [Exemptions, PermitCheck]

