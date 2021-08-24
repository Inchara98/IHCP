import configparser
from datetime import datetime

config=configparser.RawConfigParser()
config.read("/home/inchara/PycharmProjects/IHCP/Configuration/config.ini")

class ReadConfig():

    @staticmethod
    def getApplicationUrl():
        url = config.get('common_info','baseUrl')
        return url

    @staticmethod
    def getUserID():
        username = config.get('common_info','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common_info','password')
        return password

    @staticmethod
    def get_Community_FilePath():
        Community = config.get('common_info', 'Community')
        return Community

    @staticmethod
    def get_Deaconess_FilePath():
        Deaconess = config.get('common_info', 'Deaconess')
        return Deaconess

    @staticmethod
    def get_Downloads():
        Downloads = config.get('common_info', 'Downloads')
        return Downloads

    @staticmethod
    def get_date():
        current_time = datetime.now()
        date_formate = current_time.strftime('%m/%d')
        year = current_time.strftime('%y')
        date = date_formate.replace('/', '') + year + ""
        return date







