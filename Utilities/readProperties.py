import configparser
import os
from datetime import datetime

from selenium import webdriver

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
    def get_Baptist_Health_FilePath():
        Baptist_Health = config.get('common_info', 'Baptist_Health')
        return Baptist_Health

    @staticmethod
    def get_CommAnder_FilePath():
        CommAnder = config.get('common_info', 'CommAnder')
        return CommAnder

    @staticmethod
    def get_Community_VEI_FilePath():
        Community_VEI = config.get('common_info', 'Community_VEI')
        return Community_VEI

    @staticmethod
    def get_Daviess_FilePath():
        Daviess = config.get('common_info', 'Daviess')
        return Daviess

    @staticmethod
    def get_Gibson_FilePath():
        Deaconess = config.get('common_info', 'Deaconess')
        return Deaconess

    @staticmethod
    def get_GoodSam_FilePath():
        GoodSam = config.get('common_info', 'GoodSam')
        return GoodSam

    @staticmethod
    def get_Goshen_FilePath():
        Goshen = config.get('common_info', 'Goshen')
        return Goshen

    @staticmethod
    def get_gsFhc_FilePath():
        gsFhc = config.get('common_info', 'gsFhc')
        return gsFhc

    @staticmethod
    def get_Harrison_County_FilePath():
        Harrison_County = config.get('common_info', 'Harrison_County')
        return Harrison_County

    @staticmethod
    def get_Kings_FilePath():
        Kings = config.get('common_info', 'Kings')
        return Kings

    @staticmethod
    def get_Methodist_FilePath():
        Methodist= config.get('common_info', 'Methodist')
        return Methodist

    @staticmethod
    def get_Parkview_FilePath():
        Parkview = config.get('common_info', 'Parkview')
        return Parkview

    @staticmethod
    def get_Putnam_FilePath():
        Putnam = config.get('common_info', 'Putnam')
        return Putnam

    @staticmethod
    def get_REID_FilePath():
        REID = config.get('common_info', 'REID')
        return REID

    @staticmethod
    def get_Riverview_FilePath():
        Riverview = config.get('common_info', 'Riverview')
        return Riverview

    @staticmethod
    def get_The_Womens_FilePath():
        The_Womens = config.get('common_info', 'The_Womens')
        return The_Womens

    @staticmethod
    def get_UNION_FilePath():
        UNION = config.get('common_info', 'UNION')
        return UNION

    @staticmethod
    def get_UTMC_FilePath():
        UTMC = config.get('common_info', 'UTMC')
        return UTMC

    @staticmethod
    def get_Wabash_FilePath():
        Wabash= config.get('common_info', 'Wabash')
        return Wabash

    @staticmethod
    def get_date():
        current_time = datetime.now()
        date_formate = current_time.strftime('%m/%d')
        year = current_time.strftime('%y')
        date = date_formate.replace('/', '') + year + ""
        return date
