import time
from selenium import webdriver
from Page_of_objects.Login_Page import LoginPage
from Utilities.readProperties import ReadConfig

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()
    Community = ReadConfig.get_Community_FilePath()
    Deaconess = ReadConfig.get_Deaconess_FilePath()
    Baptist_Health = ReadConfig.get_Baptist_Health_FilePath()
    CommAnder = ReadConfig.get_CommAnder_FilePath()
    Community_VEI = ReadConfig.get_Community_VEI_FilePath()
    Daviess = ReadConfig.get_Daviess_FilePath()
    Gibson = ReadConfig.get_Gibson_FilePath()
    GoodSam = ReadConfig.get_GoodSam_FilePath()
    Goshen = ReadConfig.get_Goshen_FilePath()
    gsFhc = ReadConfig.get_gsFhc_FilePath()
    Harrison_County = ReadConfig.get_Harrison_County_FilePath()
    Kings = ReadConfig.get_Kings_FilePath()
    Methodist = ReadConfig.get_Methodist_FilePath()
    Parkview = ReadConfig.get_Parkview_FilePath()
    Putnam = ReadConfig.get_Putnam_FilePath()
    REID = ReadConfig.get_REID_FilePath()
    Riverview = ReadConfig.get_Riverview_FilePath()
    The_Womens = ReadConfig.get_The_Womens_FilePath()
    UNION = ReadConfig.get_UNION_FilePath()
    UTMC = ReadConfig.get_UTMC_FilePath()
    Wabash = ReadConfig.get_Wabash_FilePath()

    date = ReadConfig.get_date()

    def test_login(self):
        self.driver = webdriver.Chrome(executable_path="")
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.Advance()
        self.lp.Proceed_link()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.lp.field_gotofolder()
        time.sleep(10)
        self.lp.Upload_Wizard()
        time.sleep(4)
        add_files = self.lp.addfiles()
        if len(self.Community) != 0:
            add_files.send_keys(self.Community+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.Deaconess) != 0:
            add_files.send_keys(self.Deaconess+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.Baptist_Health) != 0:
            add_files.send_keys(self.Baptist_Health+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.CommAnder) != 0:
            add_files.send_keys(self.CommAnder+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.Community_VEI) != 0:
            add_files.send_keys(self.Community_VEI+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.Daviess) != 0:
            add_files.send_keys(self.Daviess+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.Gibson) != 0:
            add_files.send_keys(self.Gibson+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.GoodSam) != 0:
            add_files.send_keys(self.GoodSam+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.Goshen) != 0:
            add_files.send_keys(self.Goshen+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.gsFhc) != 0:
            add_files.send_keys(self.gsFhc+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.Harrison_County) != 0:
            add_files.send_keys(self.Harrison_County+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.Kings)  != 0:
            add_files.send_keys(self.Kings+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.Methodist) != 0:
            add_files.send_keys(self.Methodist+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.Parkview)  != 0:
            add_files.send_keys(self.Parkview+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.Putnam)  != 0:
            add_files.send_keys(self.Putnam+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.REID)  != 0:
            add_files.send_keys(self.REID+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.Riverview) != 0:
            add_files.send_keys(self.Riverview+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.The_Womens) != 0:
            add_files.send_keys(self.The_Womens+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.UNION) != 0:
            add_files.send_keys(self.UNION+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.UTMC) != 0:
            add_files.send_keys(self.UTMC+self.date)
            time.sleep(2)
        else:
            pass
        if len(self.Wabash) != 0:
            add_files.send_keys(self.Wabash+self.date)
            time.sleep(2)
        else:
            pass
        self.lp.uploadfiles()
        time.sleep(100)
        self.driver.close()


