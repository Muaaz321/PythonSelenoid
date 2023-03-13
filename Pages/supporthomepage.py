from selenium.webdriver.common.by import By
from Core.useraction import useraction
from selenium.webdriver.common.keys import Keys

from Pages.homepage import homepage


class supporthomepage(useraction):

    def __init__(self, driver):
        super().__init__(driver)

    userac = useraction(None)

    gateway_search_txtbox = (By.XPATH, userac.locators["SupportHomepage"]["gateway_search"])
    gateway_search_button = (By.XPATH, userac.locators["SupportHomepage"]["gateway_search_button"])
    logout = (By.XPATH,"//p[text() = 'Logout']")
    popup = (By.XPATH,"//span[contains(text(),'YES')]")

    def search_gatewayemail(self, gatewayemail):
        self.action_send_keys(self.gateway_search_txtbox, gatewayemail)
        self.action_send_keys(self.gateway_search_txtbox, Keys.RETURN)
        return homepage(self.driver)


    def clickLogout(self):
        from Pages.loginpage import loginpage
        self.action_click(self.logout)
        self.action_click(self.popup)
        return loginpage(self.driver)