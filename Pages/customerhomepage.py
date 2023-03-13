import time

from selenium.webdriver.common.by import By
from Core.useraction import useraction

from Pages.securitypage import securitypage


class customerhomepage(useraction):

    def __init__(self, driver):
        super().__init__(driver)

    userac = useraction(None)

    parental_control = (By.XPATH,"//p[text() = 'Parental Control']")
    security = (By.XPATH,"//p[text() = 'Security']")
    logout = (By.XPATH,"//p[text() = 'Logout']")
    popup = (By.XPATH,"//span[contains(text(),'YES')]")

    def clickParentalControl(self):
        self.action_click(self.parental_control)

    def clickSecurity(self):
        self.action_click(self.security)
        return securitypage(self.driver)

    def clickLogout(self):
        from Pages.loginpage import loginpage
        time.sleep(10)
        self.action_click(self.logout)
        self.action_click(self.popup)
        return loginpage(self.driver)