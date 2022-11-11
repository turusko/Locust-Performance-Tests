from .load_environment import load_environment_file


def get_environment_value(key: str) -> str:
    environment = load_environment_file()
    for i in environment.values:
        if i.key == key:
            return i.value
