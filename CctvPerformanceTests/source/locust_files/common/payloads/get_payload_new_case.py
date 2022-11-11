from ..models import CCTVConfig
import uuid
from enviroment_loader import get_environment_value


def get_payload_new_case() -> dict:
    cctv_config_data = CCTVConfig(
        get_environment_value("ClientDebtTypeId"),
        get_environment_value("CameraId"),
        get_environment_value("LocationId"),
        get_environment_value("ContraventionTypeId"),
        get_environment_value("OperatorId"),
        get_environment_value("QuestionId"),
    )

    return {
        "UniqueEventReference": f"{str(uuid.uuid4())}",
        "ClientDebtType": f"{cctv_config_data.client_debt_type_field_id}",
        "VehicleLicencePlate": "YAZ692",
        "VehicleMake": "Ford",
        "VehicleModel": "Focus",
        "VehicleColour": "Blue",
        "DiplomaticVehicle": False,
        "ForeignVehicle": False,
        "CameraID": f"{cctv_config_data.camera_id}",
        "LocationId": f"{cctv_config_data.location_id}",
        "ContraventionTypeId": f"{cctv_config_data.contravention_type_id}",
        "ContraventionDateTime": "2021-06-10T14:40:41.107",
        "FullFineAmount": 130,
        "OperatorId": f"{cctv_config_data.operator_id}",
        # "QuestionResponses": [
        #     {
        #         "QuestionId": f"{cctv_config_data.question_id}",
        #         "QuestionResponseValue": "CEO Comments"
        #     }
        # ]
    }
