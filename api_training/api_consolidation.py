import unittest

from api_training import first_api_test


class Test_Get_API(unittest.TestCase):
    def test_get_page_2_api_information(self):
        function1 = first_api_test.test_get_user_2_details()
        return function1

