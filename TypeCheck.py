import re
import datetime

def is_list(var_to_check):
    return isinstance(var_to_check, list)


def is_int(var_to_check):
    return isinstance(var_to_check, int)


def is_string(var_to_check):
    return isinstance(var_to_check, str)


def is_bool(var_to_check):
    return isinstance(var_to_check, bool)


def is_mail(var_to_check):
    email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return is_string(var_to_check) and re.search(email_regex, var_to_check)


def is_date(var_to_check):
    try:
        if datetime.datetime.strptime(var_to_check, '%d-%m-%Y'):
            return True
    except ValueError:
        return False
        # raise ValueError("Incorrect data format, should be dd-mm-yyyy")


def is_uuid(var_to_check):
    if re.match("^[A-Za-z0-9-]*$", var_to_check):
        return True
    else:
        return False


def is_auth_token(var_to_check):
    if re.match("^Bearer [A-Za-z0-9]*$", var_to_check):
        return True
    else:
        return False


switch = {
    'Int': is_int,
    'String': is_string,
    'Email': is_mail,
    'Date': is_date,
    'UUID': is_uuid,
    'Boolean': is_bool,
    'Auth-Token': is_auth_token,
    'List':is_list
}


def check_param(input_param_value, types):
    results = []
    for param_type in types:
        result = switch[param_type](input_param_value)
        results.append(result)
    return all(results)
