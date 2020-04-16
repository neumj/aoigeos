import json


def read_json(file_path):
    with open(file_path) as json_data:
        d = json.load(json_data)
    return d


def write_json(data_dict,file_path):
    with open(file_path, 'w') as fp:
        json.dump(data_dict, fp, indent=4)