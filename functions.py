import configparser
import os

from directory_path import path_location

config = configparser.RawConfigParser()
config.read("../configurations/config.ini")


class reusable_functions:

    """ Method returns the api_url from config.ini """
    @staticmethod
    def get_api_url():
        return config.get('config', 'api_url')

    """ Method returns username from config.ini """
    @staticmethod
    def get_username():
        return config['config']['username']

    """ Method returns password from config.ini """
    @staticmethod
    def get_password():
        return config['config']['password']

    @staticmethod
    def get_validation_of_get_api_responses(response):
        count = 0
        ''' Validate the response code the api '''
        if response.status_code == 200:
            print("API is working as expected ", response.status_code)
        else:
            count = count + 1
        if response.text != {}:
            print("API is provided the response", response.text)
        else:
            count = count + 1
        if response.elapsed != 200:
            print('API Response :', response.elapsed)
        else:
            count = count + 1

        if 'application/json' in response.headers['Content-Type']:
            print("API Response is in JSON Format", response.headers['Content-Type'])
        else:
            print("Response is not in JSON Format",response.headers['Content-Type'])
            count = count + 1
        return count

    @staticmethod
    def get_validation_of_post_api_responses(response):
        count = 0
        ''' Validate the response code the api '''
        if response.status_code == 201 or 200:
            print("API is working as expected ", response.status_code)
        else:
            count = count + 1
        if response.text != {}:
            print("API is provided the response", response.text)
        else:
            count = count + 1

        """ Validate the Response code of API Response """
        if response.elapsed != 200:
            print('API Response :', response.elapsed)
        else:
            count = count + 1
            print('Response Time is exceeds : ', response.elapsed)

        ''' Validate the response is in json format '''
        if 'application/json' in response.headers['Content-Type']:
            print("API Response is in JSON Format", response.headers['Content-Type'])
        else:
            print("Response is not in JSON Format",response.headers['Content-Type'])
            count = count + 1
        return count

    @staticmethod
    def get_validation_of_invalid_responses(response):
        count = 0
        ''' Validate the response code the api '''
        if response.status_code == 404 or 204 or 400:
            print("API is working as expected ", response.status_code)
        else:
            print('Actual Response code', response.status_code)
            count = count + 1

        ''' Validate the time elapsed for getting api response '''
        if response.elapsed != 100:
            print('API Response :', response.elapsed)
        else:
            count = count + 1
            print('Response Time is exceeds : ', response.elapsed)

        ''' Validate the response is in json format '''
        if 'application/json' in response.headers['Content-Type']:
            print("API Response is in JSON Format", response.headers['Content-Type'])
        else:
            print("Response is not in JSON Format", response.headers['Content-Type'])
            count = count + 1
        return count

    @staticmethod
    def get_delete_method_api_responses(response):
        count = 0
        ''' Validate the response code the api '''
        if response.status_code == 404 or 204 or 400:
            print("API is working as expected ", response.status_code)
        else:
            print('Actual Response code', response.status_code)
            count = count + 1

        ''' Validate the time elapsed for getting api response '''
        if response.elapsed != 100:
            print('API Response :', response.elapsed)
        else:
            count = count + 1
            print('Response Time is exceeds : ', response.elapsed)
        return count

    @staticmethod
    def get_validate_error_responses(response):
        count = 0
        ''' Validate the response code the api '''
        if response.status_code == 404 or 204 or 400:
            print("API is working as expected ", response.status_code)
        else:
            print('Actual Response code', response.status_code)
            count = count + 1
        """ Validating the response text """
        value = response.json()
        print(value)
        if value['error'] == "Missing password":
            print("Error message is showing", response.text)
        else:
            print("Error message is not showing ", response.text)
            count = count + 1
        return count

    @staticmethod
    def get_validate_the_response_fields(resp):
        count = 0
        for record in resp.json()['data']:
            if record['id'] == '' or 'null':
                count = count + 1
            if record['email'] == '' or 'null':
                count = count + 1
            if record['first_name'] == '' or 'null':
                count = count + 1
            if record['last_name'] == '' or 'null':
                count = count + 1
            if record['avatar'] == '' or 'null':
                count = count + 1
        return count
