def get_current_user(request):
    if 'current_user' in request.session and request.session['current_user']:
        return request.session['current_user']
    return None

def get_current_user_by_key(request, key):
    current_user = get_current_user(request)
    if current_user and key in current_user:
        return current_user[key]
    return None

def get_current_user_access_token(request):
    try:
        token = get_current_user_by_key(request, 'access_token')
        if not token:
            token = ""
    except:
        token = ""
    return token

def update_current_user_session(request, new_data_dict):
    user_data = get_current_user(request)
    if user_data != None:
        for k, v in new_data_dict.items():
            user_data[k] = v
        request.session['current_user'] = user_data
    else:
        store_session_login(request, new_data_dict)
    return True

def store_session_login(request, data):
    """
    with auth:
        session['current_user'] = [
            'id'
            'access_token',
            'email',
            'first_name',
            'last_name',
            'avatar',
            'checkout_id',
            'checkout_token
        ]
    no auth:
        session['current_user'] = [
            'email',
            'first_name',
            'last_name',
        ]
    """
    request.session['current_user'] = data

def is_user_authenticated(request):
    access_token = get_current_user_access_token(request)
    if access_token == "" or access_token is None:
        return False
    return True
