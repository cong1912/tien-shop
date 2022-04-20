import json
from django.conf import settings

from mysite.helpers.core_api_helper import CoreApiHelper
from ..action import Action
from mysite.helpers.auth_business import (
    get_current_user_by_key
)

class GetHomeAction(Action):
    def run(self, request):
        first = 10
        slug = "mom-and-baby-shop"
        try:
            token = get_current_user_by_key(request, 'access_token')
            if not token:
                token = ""
        except:
            token = ""
        headers = {
            "Content-Type":"application/json",
            "Authorization": "JWT " + token
        }
        
        query = """query {
                    categories(first:10,level:0) {
                        edges{
                          node{
                            name
                            slug
                            backgroundImage{
                              url
                            }
                          }
                        }
                    }
                }"""
        variables = {'slug': slug, 'first': first}
        r = CoreApiHelper.post_api(json_data={"query": query}, headers=headers)
        if self.is_api_response_success(r.json()):
            data = r.json()['data']
            result = {
                'category': data['categories']
            }
            return self.make_success(result, 'Get categoty name success')
        else:
            return self.make_error({}, '', r.status_code)
