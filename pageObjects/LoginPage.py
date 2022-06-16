from selenium.webdriver.common.by import By


class LoginPage:
    email_textbox_xpath = "//input[@name='Email' or type='email']"
    password_textbox_xpath = "//input[@name='Password' or type='password']"
    login_btn_xpath = "//button[@type='submit' and contains(text(),'Log in')]"
    logout_link = "//a[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.email_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_textbox_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_link).click()
