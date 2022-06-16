import configparser
config = configparser.RawConfigParser()
filename = r"C:\Users\Home\PycharmProjects\NewHybridProject\Configurations\config.ini"
config.read(filename)

class ReadConfig:
    @staticmethod
    def getApplication():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

