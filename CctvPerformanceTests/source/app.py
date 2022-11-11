import os
import enviroment_loader, locust_files, GUI
import json


def main():
    enviroment_loader.save_new_auth_token()
    locust_files.create_config_file()
    print("Iam here")
    os.system("python.exe -m locust")


if __name__ == '__main__':
    if GUI.run_app():
        try:
            main()
        except KeyboardInterrupt as e:
            print("program ended..")
        except json.decoder.JSONDecodeError as e:
            print("Invalid enviroment data")

            GUI.run_app()
        finally:
            locust_files.remove_locust_config_file()
