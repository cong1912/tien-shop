from django.conf import settings
from django.http import JsonResponse
import string
import random
import json
import time
from random import sample

def make_json_success(result, message, message_code = '', dev_message = '', code = 200):
    response = {
        'success' : True,
        'message' : message,
        'data' : result,
        'status_code' : code,
        'message_code' : message_code,
        'dev_message' : dev_message
    }
    return JsonResponse(response)
    
def make_json_error(error_arr, error_msg, message_code = '', dev_message = '', code = 400):
    if len(error_arr) > 0:
        code = 400
        if error_msg == None or error_msg == '':
            if 'code' in error_arr:
                error_msg = _(error_arr['code'])
    else:
        code = 500
    response = {
        'success' : False,
        'message' : error_msg,
        'status_code' : code,
        'message_code' : message_code,
        'dev_message' : dev_message,
        'data' : []
    }
    if error_arr:
        response['data'] = error_arr
    return JsonResponse(response)

def convert_query_dict_to_dict(query_dict):
    return dict(query_dict.lists())

def convert_query_dict_to_dict_object(query_dict):
    converted = {}
    origin = dict(query_dict.lists())
    for k, v in origin.items():
        if len(v) == 1:
            converted[k] = v[0]
        else:
            converted[k] = v
    return converted

def convert_address_dict(key_a, key_b, data):
    del data[key_a]
    del data[key_b]
    return data

def get_img_url_display_test(origin_url, is_custom_size = True, width = 120, height = 120):
    if origin_url == None or origin_url == '' or '/static/images/' in origin_url:
        return '/mysite/static/public/assets/images/product/default.png'
    extenstion_index = origin_url.rfind(".")
    extenstion = ''
    if extenstion_index != None:
        extenstion = origin_url[extenstion_index:len(origin_url)]
    url = origin_url
    if get_core_api_app_url() in origin_url and "/media/" in origin_url:
        if '__sized__' not in origin_url:
            path = origin_url.replace(extenstion, "").replace(get_core_api_app_url(), "").replace("/media/", "")
            if is_custom_size == True:
                url = settings.PUBLIC_API_APP_URL + '/media/__sized__/' + path + '-thumbnail-' + str(width) + 'x' + str(height) + '-70' + extenstion
            else:
                url = settings.PUBLIC_API_APP_URL + "/media/" + path + extenstion
        else:
            url = origin_url.replace(get_core_api_app_url(), settings.PUBLIC_API_APP_URL)
    return url

def get_img_url_display(origin_url, is_custom_size = True, width = 120, height = 120):
    if origin_url == None or origin_url == '' or '/static/images/' in origin_url:
        return '/mysite/static/public/assets/images/product/default.png'
    return origin_url.replace(get_core_api_app_url(), settings.PUBLIC_API_APP_URL)

def get_core_api_app_url():
    url = settings.CORE_API_URL.replace("/graphql/", "")
    return url

def random_string(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def current_milli_time():
    return round(time.time() * 1000)

def get_or_gen_guest_token_session(request):
    guest_token_session = ''
    if 'guest_token' in request.session and request.session['guest_token'] is not None:
        guest_token_session = request.session['guest_token']
    else:
        guest_token_session = random_string(8) + str(current_milli_time())
        request.session['guest_token'] = guest_token_session
    return guest_token_session

def api_app_url():
    url = settings.PUBLIC_API_APP_URL + "/graphql/"
    return url

def public_api_app_url():
    url = settings.PUBLIC_API_APP_URL
    return url

def random_password():
    return random_string(size=8)

def url_param_regex(param_name, regex = '[0-9A-Za-z_\-]+'):
    return "(?P<" + param_name + ">" + regex  + ")"

def append_to_default_header_helper(additional_headers):
    default_header = {
        "Content-Type":"application/json"
    }
    if isinstance(additional_headers, dict):
       for k, v in additional_headers.items():
           default_header[k] = v
    return default_header

def log_dict(dict_var):
    if isinstance(dict_var, dict):
        print(json.dumps(dict_var, sort_keys=False, indent=2))
    elif isinstance(dict_var, list):
        print(dict_var)
    else:
        print(dict_var)

def random_code_veryfi():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr_num_veryfi = sample(numbers, 6)
    num_str_veryfi = ''
    for i in arr_num_veryfi:
        num_str_veryfi += str(i)
    return num_str_veryfi

def delivery_status(x):
    if (x == 'all-tab'):
        return ["WAITING_CONFIRM", "DELIVERY_DELAY", "ON_DELIVERY", "FULFILLED", "UNFULFILLED"]
    elif (x == 'waiting-tab'):
        return ["WAITING_CONFIRM", "DELIVERY_DELAY", "ON_DELIVERY"]
    elif (x == 'done-tab'):
        return ["FULFILLED"]
    else:
        return ["UNFULFILLED"]

def get_plugin_value_by_name(data, field):
    if len(data) > 0: 
        for value in data:
            if value['name'] == field:
                return value['value']
    return ""
