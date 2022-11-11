import unittest
import shutil
import os
from source import GUI
from source import enviroment_loader
from source import static_data
from source import locust_files


class LoadTestConfig(unittest.TestCase):

    def test_load_config(self):
        shutil.copy("./source/config.json","config.json")
        app_settings = enviroment_loader.load_application_settings()
        if os.path.exists("config.json"):
            os.remove("config.json")

if __name__ == '__main__':
    unittest.main()