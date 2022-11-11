import dataclasses
import dataclasses_json
import typing


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ApplicationSettings:
    locust_config_filename: str
    report_filename: str
    run_time: str
    users: int
    spawn_rate: int
    environment_filename: str
    max_cases: typing.Optional[int] = None
    max_wait: typing.Optional[int] = None
