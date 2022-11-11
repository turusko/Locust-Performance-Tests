
from .models import EnvironmentDetails
from .load_app_settings import load_application_settings


def load_environment_file() -> EnvironmentDetails:
    application_settings = load_application_settings()
    with open(application_settings.environment_filename, "r") as open_file:
        output = EnvironmentDetails.from_json(open_file.read())
    return output
    

