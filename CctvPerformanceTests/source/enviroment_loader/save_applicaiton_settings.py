import json
from .models import ApplicationSettings


def save_application_settings(application_settings: ApplicationSettings):
    with open("config.json", "w") as open_file:
        json.dump(application_settings.to_dict(), open_file)
