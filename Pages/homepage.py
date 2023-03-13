import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Core.useraction import useraction
from Pages.routerpage import routerpage


class homepage(useraction):

    def __init__(self, driver):
        super().__init__(driver)

    userac = useraction(None)

    user_name = (By.XPATH,userac.locators["Homepage"]["user_name"])
    gateway_search = (By.XPATH,userac.locators["Homepage"]["gateway_search"])
    gateway_search_txtbox = (By.XPATH, userac.locators["Homepage"]["gateway_search"])
    gateway_search_button = (By.XPATH, userac.locators["Homepage"]["gateway_search_button"])
    online_devices = (By.XPATH, userac.locators["Homepage"]["online_devices"])
    logout = (By.XPATH,"//img[@src='assets/x-icons/signout.svg']")
    popup = (By.XPATH, "//span[contains(text(),'YES')]")

    def get_title(self,title):
        return self.action_get_title(title)

    def is_search_gateway_exist(self):
        return self.action_is_visible(self.gateway_search)

    def get_username(self):
        if self.action_is_visible(self.user_name):
            return self.action_get_text(self.user_name)

    def search_gateway(self,gatewayparameter):
        self.action_send_keys(self.gateway_search_txtbox,gatewayparameter)
        self.action_click(self.gateway_search_button)

    def navigate_to_onlinedevice(self):
        try:
            self.action_click(self.online_devices)
        except:
            print("Couldnt click Online Device Section ++++++++++++++++++++++++++ ")


    def clickGatewayrecord(self, gatewaypara):

        gatewayRecord = (By.XPATH, "//td[contains(text(),'" + gatewaypara + "')]")
        self.action_click(gatewayRecord)
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        return routerpage(self.driver)


    def clickLogout(self):
        from Pages.loginpage import loginpage

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.action_click(self.logout)
        time.sleep(5)
        self.action_click(self.popup)
        return loginpage(self.driver)

