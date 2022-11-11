
import enviroment_loader
from enviroment_loader import load_application_settings
import PySimpleGUI as sg



def save_applcation(enviroment_filename: str, max_cases: int, max_wait: int):
    application_settings = load_application_settings()
    application_settings.environment_filename = enviroment_filename
    application_settings.max_cases = max_cases
    application_settings.max_wait = max_wait
    enviroment_loader.save_application_settings(application_settings)

def get_environment_filename():
    application_settings = load_application_settings()
    return application_settings.environment_filename

def get_wait_time() -> str:
    if load_application_settings().max_wait == None:
        return "1"
    else:
        return str(load_application_settings().max_wait)

def get_max_cases() -> str:
    if load_application_settings().max_cases == None:
        return "1"
    else:
        return str(load_application_settings().max_cases)


def run_app():
    text_string = get_environment_filename()
    file = text_string.split("/")[len(text_string.split("/"))-1]
    app_text = """The following application emulates CiteWeb batch upload single thread"""
    

    sg.theme('Reddit')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text(app_text)],
                [sg.Text('Select Postman Enviroment File')],
                [sg.Text(key="file_display_name", text=f'Currently Selected file: {file}')],
                [sg.Input(key="file_locaiton", default_text=text_string, enable_events=True, readonly=True), sg.FileBrowse()],
                [sg.Text("Enter max cases: "), sg.Input(key="max_cases", default_text=get_max_cases(), size=(5,1))],
                [sg.Text("Enter max wait: "), sg.Input(key="max_wait", default_text=get_wait_time(), size=(5,1))],
                [sg.Text('')],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window

    window = sg.Window('CCTV Performance', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            window.close()
            return False
        if event == "Ok":
            try:
                max_cases = int(window["max_cases"].get())
                max_wait = int(window["max_wait"].get())
                fileNameDisplay = window["file_locaiton"].get()
                save_applcation(fileNameDisplay, max_cases, max_wait)
                window.close()
                return True
            except ValueError as e:
                sg.popup(f'wait and cases can only be a number')
        if event == 0:
            window["file_display_name"].update(value="Currently Selected file: "+values[0].split("/")[len(values[0].split("/"))-1])


    
