import json
import requests
from cerberus import Validator


def test_get_user_2_details():
    url = "https://reqres.in/api/users?page=2"
    payload = ""
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json.loads(response.text)

    ''' Validate the Response schema '''
    schema = {
                "id": {'type': 'integer'},
                "email": {'type': 'string'},
                "first_name": {'type': 'string'},
                "last_name": {'type': 'string'},
                "avatar": {'type': 'string'}
            }
    validator = Validator(schema)
    is_valid = validator.validate(result['data'][0])
    print('schema result', is_valid)
    print(result['data'][0])
    if is_valid:
        print("Schema is validated it is as expected")
    else:
        print('schema is not matching ')
        assert False

    ''' Validate the response code'''
    if response.status_code == 200:
        print("API is Working as expected ", response.status_code)
    else:
        print('API Response code is not matched ', response.status_code)
        assert False

    '''Validate the Response having information/data or not '''
    if response.json() != {}:
        print('Response Data is not empty ', response.json())
    else:
        assert False

    '''Checking the API Response time is less than 200ms '''
    if response.elapsed != 200:
        print('API Response :', response.elapsed)
    else:
        assert False

    '''Validating the Response in the json format or not '''
    if 'application/json' in response.headers['Content-Type']:
        print("API Response is in JSON Format", response.headers['Content-Type'])
    else:
        print("Response is not in JSON Format", response.headers['Content-Type'])
        assert False

