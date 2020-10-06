import json
import Globals
import logging

def load_models_file(file_path):
    with open(file_path) as json_file:
        return json.load(json_file)

def get_key(json):
    key = json['path']+json['method']
    return key



def load_models_to_dict(input_data):
    if type(input_data) is list:
        for model in input_data:
            load_model(model, Globals.models_dict)
    else:
        load_model(input_data,Globals.models_dict)

def load_model(model, models_dict):
    key = model["path"] + model["method"]
    new_model = {}
    for attr in Globals.ATTRIBUTES_TO_CHECK:
        new_model[attr] = {}
        new_model[attr]["required"] = {}
        new_model[attr]["optional"] = {}
        for param in model[attr]:
            param_name = param["name"]
            param_types = param["types"]
            if param["required"]:
                new_model[attr]["required"][param_name] = param_types
            else:  # param is not required
                new_model[attr]["optional"][param_name] = param_types
    models_dict[key] = new_model





def load_josn_from_string(query_data):
    try:
        return json.loads(query_data)
    except Exception as ex:
        logging.error("Can't Convert Data to JSON")
        return None








