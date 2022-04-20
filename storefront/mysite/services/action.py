from django.utils.translation import gettext as _

from mysite.helpers.common_business import (
    append_to_default_header_helper
)
from mysite.message_code import msg_codes

class Action:
    def make_success(self, result, message, message_code = '', dev_message = '', code = 200):
        response = {
            'success' : True,
            'message' : message,
            'data' : result,
            'status_code' : code,
            'message_code' : message_code,
            'dev_message' : dev_message
        }
        return response
    
    def make_error(self, error_arr, error_msg, message_code = '', dev_message = '', code = 400):
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
        return response
    
    def is_api_response_success(self, response, root_key = None, error_key = None):
        if 'data' in response and 'error' not in response:
            if root_key != None and root_key != '' and error_key != None and error_key != '':
                is_success, error_data_return = self.is_api_response_success_advance(response, root_key, error_key)
                return is_success
            return True
        return False
    
    def is_api_response_success_advance(self, response, data_path_to_check = None, error_path_to_check = None):
        try:
            res_data = response['data']
        except KeyError:
            return False, False, {}
        d = response['data']

        is_success = True
        is_data_exist = True
        if data_path_to_check != None and data_path_to_check != '':
            data_index_list = data_path_to_check.split('/')
            if len(data_index_list) == 1:
                data_index = data_index_list[0]
                if data_index in d:
                    is_success = True
                    if d[data_index] is not None:
                        is_data_exist = True
                    else:
                        is_data_exist = False
                else:
                    is_success = False
            else:
                try:
                    if d[data_index_list[0]] is not None and data_index_list[1] in d[data_index_list[0]]:
                        is_success = True
                        if d[data_index_list[0]][data_index_list[1]] is not None:
                            is_data_exist = True
                        else:
                            is_data_exist = False
                    else:
                        is_success = False
                except KeyError:
                    is_success = False


        error = {}
        error_data = None
        if is_success == False and error_path_to_check != None and error_path_to_check != '':
            data_index_list = error_path_to_check.split('/')
            if len(data_index_list) == 1:
                data_index = data_index_list[0]
                if data_index in d and d[data_index] is not None and len(d[data_index]) > 0:
                    error_data = d[data_index]
            else:
                if data_index_list[0] in d and data_index_list[1] in d[data_index_list[0]] and d[data_index_list[0]][data_index_list[1]] is not None:
                    error_data = d[data_index_list[0]][data_index_list[1]]
        if error_data is not None and len(error_data) > 0:
            error = error_data[0]
        return is_success, is_data_exist, error

    def append_to_default_header(self, additional_headers):
        return append_to_default_header_helper(additional_headers)

    def prepare_action_response(self, r, success_code, data_path_to_check = None, error_path_to_check = None):
        is_success, is_data_exist, error = self.is_api_response_success_advance(r.json(), data_path_to_check, error_path_to_check)
        if is_success:
            data = r.json()['data']
            if is_data_exist:
                return self.make_success(data, '', success_code)
            else:
                return self.make_success(data, '', msg_codes.DATA_NOT_FOUND_CODE)
        else:
            return self.make_error(error, '', _(msg_codes.SERVER_ERROR_CODE), msg_codes.SERVER_ERROR_CODE, 500)
