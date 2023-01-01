

import unittest

from API_Requests import post_method_apis


class Test_PostAPI(unittest.TestCase):
    def test_creation_of_user_using_post_method(self):
        api_function = post_method_apis.test_creation_of_user_using_post_method()
        return api_function

    def test_modify_of_userinfo_using_put_method(self):
        api_function = post_method_apis.test_modify_of_userinfo_using_put_method()
        return api_function

    def test_modify_of_userinfo_using_patch_method(self):
        api_function = post_method_apis.test_modify_of_userinfo_using_patch_method()
        return api_function

    def test_delete_information_using_delete_method(self):
        api_function = post_method_apis.test_delete_information_using_delete_method()
        return api_function

    def test_login_using_post_method(self):
        api_function = post_method_apis.test_login_using_post_method()
        return api_function

    def test_error_message_using_post_method(self):
        api_function = post_method_apis.test_error_message_using_post_method()
        return api_function

    def test_token_by_login_using_post_method(self):
        api_function = post_method_apis.test_token_by_login_using_post_method()
        return api_function

    def test_error_message_at_login_using_post_method(self):
        api_function = post_method_apis.test_error_message_at_login_using_post_method()
        return api_function



if __name__ == '__main__':
    unittest.main()
