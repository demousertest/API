import configparser
config = configparser.ConfigParser()
config.read(f'../configurations/config.ini')

class Readconfig:

    @staticmethod
    def get_admin_page_url():
        url = config.get('admin login info', 'admin_page_url')
        return url
    @staticmethod
    def get_admin_username():
        username = config.get('admin login info', 'username')
        return username

    @staticmethod
    def get_admin_password():
        password = config.get('admin login info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('admin login info', 'invalid_username')
        return invalid_username

