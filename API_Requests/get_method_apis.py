import json
import time

import requests

from functions import reusable_functions


def test_get_page_2_api_information():
    reuse = reusable_functions()
    payload = {}
    headers = {}
    path = 'users?page=2'
    url = reuse.get_api_url() + path
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json.dumps(response.text)
    print("Json Format Data: ", result)
    result1 = reuse.get_validation_of_get_api_responses(response)
    if result1 == 0:
        print('API is working as Expected')
        assert True
    else:
        assert False

    # result2 = reuse.get_validate_the_response_fields(response)
    # if result2 == 0:
    #     print('API Response showing as Expected')
    #     assert True
    # else:
    #     assert False


def test_api_to_get_specific_user_details():
    reuse = reusable_functions()
    payload = {}
    headers = {}
    path = 'users/2'
    url = reuse.get_api_url() + path
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json.dumps(response.text)
    print("Json Format Data: ", result)
    result = reuse.get_validation_of_get_api_responses(response)
    if result == 0:
        print('API is working as expected')
        assert True
    else:
        assert False


def test_api_to_get_invalid_user_details_by_id():
    reuse = reusable_functions()
    payload = {}
    headers = {}
    path = 'users/23'
    url = reuse.get_api_url() + path
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json.dumps(response.text)
    print("Json Format Data: ", result)
    result = reuse.get_validation_of_invalid_responses(response)
    if result == 0:
        print('API is working as expected')
        assert True
    else:
        assert False


def test_api_to_get_unknown_user_details_by_id():
    reuse = reusable_functions()
    payload = {}
    headers = {}
    path = 'unknown'
    url = reuse.get_api_url() + path
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json.dumps(response.text)
    print("Json Format Data: ", result)
    result = reuse.get_validation_of_get_api_responses(response)
    if result == 0:
        print('API is working as expected')
        assert True
    else:
        assert False


def test_api_to_get_unknown_specified_user_details():
    reuse = reusable_functions()
    payload = {}
    headers = {}
    path = 'unknown/2'
    url = reuse.get_api_url() + path
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json.dumps(response.text)
    print("Json Format Data: ", result)
    result = reuse.get_validation_of_get_api_responses(response)
    if result == 0:
        print('API is working as expected')
        assert True
    else:
        assert False


def test_api_to_get_invalid_unknown_details_by_id():
    reuse = reusable_functions()
    payload = {}
    headers = {}
    path = 'unknown/23'
    url = reuse.get_api_url() + path
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json.dumps(response.text)
    print("Json Format Data: ", result)
    result = reuse.get_validation_of_invalid_responses(response)
    if result == 0:
        print('API is working as expected')
        assert True
    else:
        assert False


def test_api_to_get_all_user_details():
    reuse = reusable_functions()
    payload = {}
    headers = {}
    path = 'users'
    url = reuse.get_api_url() + path
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json.dumps(response.text)
    print("Json Format Data: ", result)
    result = reuse.get_validation_of_get_api_responses(response)
    if result == 0:
        print('API is working as expected')
        assert True
    else:
        assert False


def test_delay_response_using_Delay():
    reuse = reusable_functions()
    n = 10
    payload = {}
    headers = {}
    value = "delay=" + str(n) + ""
    print(value)
    path = "users?"
    url = reuse.get_api_url() + path + value
    print(url)
    start = time.time()
    print('start', start)
    response = requests.request("GET", url, headers=headers, data=payload)
    end = time.time()
    print('end', end)
    result = json.dumps(response.text)
    print("Json Format Data: ", result)
    result = reuse.get_validation_of_get_api_responses(response)
    if result == 0:
        print('API is working as expected')
        assert True
    else:
        assert False

