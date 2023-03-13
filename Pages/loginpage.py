import time

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from Core.useraction import useraction
from Pages.homepage import homepage
from Pages.supporthomepage import supporthomepage
from Tests.conftest import BASEURL, locator_data

class loginpage(useraction):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(BASEURL)

    userac = useraction(None)

    username_txtbox = (By.XPATH,userac.locators["Loginpage"]["username_text_box"])
    password_txtbox = (By.XPATH,userac.locators["Loginpage"]["password_text_box"])
    submit_button = (By.XPATH,userac.locators["Loginpage"]["login_button"])
    register_button = (By.XPATH,userac.locators["Loginpage"]["register_button"])
    gateway_button = (By.XPATH,"//span[@class='ng-star-inserted']")

    """Page actions """
    def is_register_button_visible(self):
        return self.action_is_visible(self.register_button)


    def setUsername(self, usernm):
        self.action_send_keys(self.username_txtbox,usernm)


    def setPassword(self, pwd):
        self.action_send_keys(self.password_txtbox,pwd)

    def clickLogin(self):
        self.action_click(self.submit_button)

    def clickGateway(self):
        from Pages.customerhomepage import customerhomepage
        try:
            self.action_click(self.gateway_button)
            return customerhomepage(self.driver)
        except WebDriverException as e:
            raise e

    def login(self,username,password):
        self.action_send_keys(self.username_txtbox,username)
        self.action_send_keys(self.password_txtbox,password)
        self.action_click(self.submit_button)
        return homepage(self.driver)

    def login_support(self,username,password):
        self.action_send_keys(self.username_txtbox,username)
        self.action_send_keys(self.password_txtbox,password)
        self.action_click(self.submit_button)
        return supporthomepage(self.driver)