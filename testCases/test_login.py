from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplication()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_home_page_title(self, setup):

        self.logger.info("******************** Test_001_Login ********************")
        self.logger.info("******************** Verifying Home Page Title ********************")
        self.driver = setup
        # self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        # assert act_title == "Your store. Login"
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("******************** Home page title test is passed ********************")
            assert True
        else:
            self.driver.save_screenshot(".\\..\\Screenshots\\" + "test_home_page_title.png")
            self.driver.close()
            self.logger.error("******************** Home page title test is failed ********************")
            assert False

    def test_login(self, setup):
        self.logger.info("******************** Verifying Login test ********************")
        self.driver = setup
        # self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.login_page = LoginPage(self.driver)
        self.login_page.setUserName(self.username)
        self.login_page.setPassword(self.password)
        self.login_page.clickLogin()
        act_title = self.driver.title
        # assert act_title == "Dashboard / nopCommerce administration"
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("******************** Verifying Login test is passed ********************")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\..\\Screenshots" + "\\test_login.png")
            self.driver.close()
            self.logger.error("******************** Verifying Login test is failed ********************")
            assert False


### 32:28