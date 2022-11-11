from .models import ApplicationSettings


def load_application_settings() -> ApplicationSettings:
    with open("config.json", "r") as openfile:
        output = ApplicationSettings.from_json(openfile.read())
    return output
