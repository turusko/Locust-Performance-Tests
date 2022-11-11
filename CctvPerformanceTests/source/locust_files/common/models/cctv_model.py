import dataclasses
import dataclasses_json


@dataclasses.dataclass
class CCTVConfig:
    client_debt_type_field_id: str
    camera_id: str
    location_id: str
    contravention_type_id: str
    operator_id: str
    question_id: str


