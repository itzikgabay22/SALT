from DAL import *
import Globals
from TypeCheck import *


def check_request(json_request):
    errors =[]
    key = get_key(json_request)
    if key not in Globals.models_dict:
        errors.append("Path Or Method Does Not Exist")
        return errors
    for attr in Globals.ATTRIBUTES_TO_CHECK:
        req_params = list(Globals.models_dict[key][attr]["required"].keys())
        if attr in Globals.models_dict[key]:
            for param in json_request[attr]:
                param_name = param['name']
                param_value = param['value']
                if not (param_name in Globals.models_dict[key][attr]["optional"] or param_name in Globals.models_dict[key][attr]["required"] ) :
                    errors.append(f"paramter name: {param_name} not exist in model")
                else:
                    if param_name in Globals.models_dict[key][attr]["required"]:
                        req_params.remove(param_name)
                        param_model_types = Globals.models_dict[key][attr]["required"][param_name]
                        result = check_param(param_value, param_model_types)
                    else:
                        if param_name in Globals.models_dict[key][attr]["optional"]:
                            param_model_types = Globals.models_dict[key][attr]["optional"][param_name]
                            result = check_param(param['value'], param_model_types)
                    if not result:
                        errors.append(f"Type mismatch on param  {param_name}")
        if len(req_params) > 0:
                for parameter in req_params:
                    errors.append("Required Parameter Missed:" + parameter)
    return errors




