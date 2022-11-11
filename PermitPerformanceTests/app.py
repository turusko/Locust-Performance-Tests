import os
from time import strftime



time_stamp = strftime("%d-%m-%Y %H%M%S")
config_file_name = "locust.conf"
report_name = f'report'
host = "https://identitydev.xrxpsc.com/"
users = 1
spawn_rate = "1"

config = f"""locustfile = locustfile.py
headless = true
master = false
expect-workers = 1
host = {host}
users = {users}
spawn-rate = {spawn_rate}
run-time = 60s
html = report/{time_stamp}/{report_name}.html
csv = report/{time_stamp}/{report_name}.csv"""

if os.path.exists(config_file_name):
    os.remove(config_file_name)

if not os.path.isdir("report"):
    os.mkdir("report")

if not os.path.isdir(f"report/{time_stamp}"):
    os.mkdir(f'report/{time_stamp}')

with open(config_file_name, "w") as open_file:
    open_file.write(config)

os.system("locust")
