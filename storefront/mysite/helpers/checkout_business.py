from mysite.helpers.auth_business import (
    get_current_user,
    get_current_user_access_token,
    get_current_user_by_key
)
from mysite.helpers.common_business import (
    get_or_gen_guest_token_session
)

def get_input_data_for_request_current_cart(request):
    input_data = {}
    access_token = get_current_user_access_token(request)
    checkout_token = get_current_user_by_key(request, "checkout_token")
    checkout_id = get_current_user_by_key(request, "checkout_id")
    input_data['checkout_token'] = checkout_token
    input_data['checkout_id'] = checkout_id
    if access_token is not None and access_token != "":
        input_data['access_token'] = access_token
    else:
        guest_email = get_or_gen_guest_token_session(request) + '@guest.com'
        input_data['email'] = guest_email
    return input_data
