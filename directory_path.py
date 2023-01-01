import os


class path_location:

    """Method to return config.ini file location """
    @staticmethod
    def get_config_ini_path():
        cwd = os.path.dirname(__file__)
        ini = os.path.join(cwd, 'configurations/config.ini')
        return ini

    """ Method to return Report file location """
    @staticmethod
    def get_api_test_report():
        cwd = os.path.dirname(__file__)
        report_path = os.path.join(cwd, 'Reports/API_Result.html')
        return report_path
