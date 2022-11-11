from __future__ import annotations
import dataclasses
import dataclasses_json
import typing



@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EnvironmentDetails:
    id: str
    name: str
    values: typing.List[values]
    _postman_variable_scope: str
    _postman_exported_at: str
    _postman_exported_using: str


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class values:
    key: str
    value: str
    enabled: bool