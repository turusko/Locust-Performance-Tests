import base64


def load_image_as_binary(filename) -> str:

    with open(filename, 'rb') as file:
        contents = file.read()
    encoded = base64.b64encode(contents)
    return str(encoded, 'utf-8')

def get_media_file() -> str:
    return load_image_as_binary("static_data/images/Cat03.jpg")
