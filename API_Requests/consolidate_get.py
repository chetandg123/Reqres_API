import unittest

from API_Requests import get_method_apis


class Test_Get_API(unittest.TestCase):
    def test_get_page_2_api_information(self):
        api_function = get_method_apis.test_get_page_2_api_information()
        return api_function

    def test_api_to_get_specific_user_details(self):
        api_function = get_method_apis.test_api_to_get_specific_user_details()
        return api_function

    def test_api_to_get_unknown_user_details_by_id(self):
        api_function = get_method_apis.test_api_to_get_unknown_user_details_by_id()
        return api_function

    def test_api_to_get_unknown_specified_user_details(self):
        api_function = get_method_apis.test_api_to_get_unknown_specified_user_details()
        return api_function

    def test_api_to_get_invalid_unknown_details_by_id(self):
        api_function = get_method_apis.test_api_to_get_invalid_unknown_details_by_id()
        return api_function

    def test_delay_response_using_Delay(self):
        api_function = get_method_apis.test_delay_response_using_Delay()
        return api_function

if __name__ == '__main__':
    unittest.main()
