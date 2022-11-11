import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Auth:
    username: str
    password: str
    auth_url: str
