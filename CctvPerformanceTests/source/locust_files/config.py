import os
import enviroment_loader


def remove_locust_config_file():
    config = enviroment_loader.load_application_settings()
    if os.path.exists(config.locust_config_filename):
        os.remove(config.locust_config_filename)


def setup_report_folders(timestamp: str):

    if not os.path.isdir("c:/report"):
        os.mkdir("c:/report")

    if not os.path.isdir(f"c:/report/{timestamp}"):
        os.mkdir(f'c:/report/{timestamp}')


def create_config_file():
    timestamp = enviroment_loader.get_timestamp_string()
    application_settings = enviroment_loader.load_application_settings()
    remove_locust_config_file()
    configfile = f"""locustfile = locust_files/locustfile.py
headless = true
master = false
expect-workers = 1
host = {enviroment_loader.get_environment_value("baseUrl")}
users = {application_settings.users}
spawn-rate = {application_settings.spawn_rate}

logfile = locust.log
loglevel = ERROR
html = c:/report/{timestamp}/{application_settings.report_filename}.html
csv = c:/report/{timestamp}/{application_settings.report_filename}.csv
only-summary = false"""
# run-time = {application_settings.run_time}
    with open(application_settings.locust_config_filename, "w") as open_file:
        open_file.write(configfile)

    setup_report_folders(timestamp)
