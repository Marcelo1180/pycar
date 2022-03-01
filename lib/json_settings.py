import json


def get_settings():
    with open("/settings.json") as data_file:
        data = json.load(data_file)
    return data
