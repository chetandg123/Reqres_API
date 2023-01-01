import json
import requests
from functions import reusable_functions


def test_creation_of_user_using_post_method():
    reuse = reusable_functions()
    payload = json.dumps({
        "name": "morpheus",
        "job": "leader"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    path = 'users'
    url = reuse.get_api_url() + path
    response = requests.request("POST", url, headers=headers, data=payload)
    result = json.dumps(response.text)
    print("Json Format Data: ", result)
    result1 = reuse.get_validation_of_post_api_responses(response)
    if result1 == 0:
        print('API is working as Expected')
        assert True
    else:
        assert False


def test_modify_of_userinfo_using_put_method():
    reuse = reusable_functions()
    payload = json.dumps({
        "name": "morpheus",
        "job": "Captain"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    path = 'users/2'
    url = reuse.get_api_url() + path
    response = requests.request("PUT", url, headers=headers, data=payload)
    result = json.dumps(response.text)
    print("Json Format Data: ", result)
    result1 = reuse.get_validation_of_post_api_responses(response)
    if result1 == 0:
        print('API is working as Expected')
        assert True
    else:
        assert False


def test_modify_of_userinfo_using_patch_method():
    reuse = reusable_functions()
    payload = json.dumps({
        "name": "morpheus",
        "job": "Captain"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    path = 'users/2'
    url = reuse.get_api_url() + path
    response = requests.request("PATCH", url, headers=headers, data=payload)
    result = json.dumps(response.text)
    print("Json Format Data: ", result)
    result1 = reuse.get_validation_of_post_api_responses(response)
    if result1 == 0:
        print('API is working as Expected')
        assert True
    else:
        assert False


def test_delete_information_using_delete_method():
    reuse = reusable_functions()
    payload = json.dumps({
        "name": "morpheus",
        "job": "leader"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    path = 'users/2'
    url = reuse.get_api_url() + path
    response = requests.request("DELETE", url, headers=headers, data=payload)
    result = json.dumps(response.text)
    print("Json Format Data: ", result)
    result1 = reuse.get_delete_method_api_responses(response)
    if result1 == 0:
        print('API is working as Expected')
        assert True
    else:
        assert False


def test_login_using_post_method():
    reuse = reusable_functions()
    payload = json.dumps({
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    path = 'register'
    url = reuse.get_api_url() + path
    response = requests.request("POST", url, headers=headers, data=payload)
    result = json.dumps(response.text)
    print("Json Format Data: ", result)
    result1 = reuse.get_validation_of_post_api_responses(response)
    if result1 == 0:
        print('API is working as Expected')
        assert True
    else:
        assert False


def test_error_message_using_post_method():
    reuse = reusable_functions()
    payload = json.dumps({
        "email": "sydney@fife"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    path = 'register'
    url = reuse.get_api_url() + path
    response = requests.request("POST", url, headers=headers, data=payload)
    result = json.dumps(response.text)
    print("Json Format Data: ", result)
    result1 = reuse.get_validate_error_responses(response)
    if result1 == 0:
        print('API is working as Expected')
        assert True
    else:
        assert False


def test_token_by_login_using_post_method():
    reuse = reusable_functions()
    payload = json.dumps({
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    path = 'login'
    url = reuse.get_api_url() + path
    response = requests.request("POST", url, headers=headers, data=payload)
    result = response.json()
    print("Json Format Data: ", result)
    if result['token'] != '' or 'null':
        print("Token is generated ", result['token'])
    else:
        assert False
    result1 = reuse.get_validation_of_post_api_responses(response)
    if result1 == 0:
        print('API is working as Expected')
        assert True
    else:
        assert False


def test_error_message_at_login_using_post_method():
    reuse = reusable_functions()
    payload = json.dumps({
        "email": "peter@klaven"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    path = 'login'
    url = reuse.get_api_url() + path
    response = requests.request("POST", url, headers=headers, data=payload)
    result = json.dumps(response.text)
    print("Json Format Data: ", result)
    result1 = reuse.get_validate_error_responses(response)
    if result1 == 0:
        print('API is working as Expected')
        assert True
    else:
        assert False

