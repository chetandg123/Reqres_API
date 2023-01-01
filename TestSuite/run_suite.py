import unittest

from HTMLTestRunner import HTMLTestRunner

from API_Requests import consolidate_get, consolidate_post
from api_training import api_consolidation
from directory_path import path_location


class MyTestSuite_APIRunner(unittest.TestCase):

    @staticmethod
    def test_API_GET_TestResult():
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(
                api_consolidation.Test_Get_API)
        ])
        p = path_location()
        outfile = open(p.get_api_test_report(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='First API Test Result ',
            verbosity=1, )
        runner1.run(regression_test)
        outfile.close()

    # @staticmethod
    # def test_API_Post_TestResult():
    #     regression_test = unittest.TestSuite()
    #     regression_test.addTests([
    #         unittest.defaultTestLoader.loadTestsFromTestCase(
    #             consolidate_post.Test_PostAPI)
    #     ])
    #     p = path_location()
    #     outfile = open(p.get_api_test_report(), "a")
    #
    #     runner1 = HTMLTestRunner.HTMLTestRunner(
    #         stream=outfile,
    #         title=' POST API Test Result ',
    #         verbosity=1, )
    #     runner1.run(regression_test)
    #     outfile.close()