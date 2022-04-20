import requests
from django.conf import settings

class CoreApiHelper:
    @staticmethod
    def post_api(json_data, headers = {}, api_endpoint = settings.CORE_API_URL):
        if not headers:
            headers_ = {
                "Content-Type":"application/json",
            }
        else:
            headers_ = headers
        return requests.post(api_endpoint, json=json_data, headers=headers_)
