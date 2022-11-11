# How to run

Get the latest modules from pip
<br>
<code>pip install -r requirement.txt</code>
<br>
Running the application by <br>
<code>python app.py</code><br>
or add custom runtime<br>
<code>python app.py 5m</code><br>
default runtime is 60s
<br><br>

# What is the expected output?

A new folder will get created called reports. Each run will create a sub folder with time and date. The sub folders will contain the CSV files and one html report.

# config.json view
<code>
{<br>
    "locust_config_filename": "locust.conf",<br>
    "report_filename": "report",<br>
    "run_time": "60s",<br>
    "users": 1,<br>
    "spawn_rate": 1,<br>
    "environment_filename": ""<br>
}
</code>