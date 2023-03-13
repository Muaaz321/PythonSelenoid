from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Core.useraction import useraction


from Tests.conftest import WAIT


class securitypage(useraction):

    def __init__(self, driver):
        super().__init__(driver)

    userac = useraction(None)

    familyshield = (By.XPATH,"//span[text() = 'Family Shield']")
    adblockerphishing = (By.XPATH, "//span[text() = 'Ad Blocker / Phishing Protection']")
    safesearch = (By.XPATH, "//span[text() = 'Safe Search']")
    exitsecurity = (By.XPATH,"//span[contains(text(),'Exit')]")
    notAllowed = (By.XPATH,"//div[contains(text(),'Not Allowed ')]")

    def get_title(self,title):
        return self.action_get_title(title)

    def clickFamilyshield(self):
        self.action_click(self.familyshield)
        WebDriverWait(self.driver,WAIT)

    def clickAdblockerphishing(self):
        self.action_click(self.adblockerphishing)

    def clickSafesearch(self):
        self.action_click(self.safesearch)

    def clickExitSecurity(self):
        from Pages.customerhomepage import customerhomepage
        self.action_click(self.exitsecurity)
        return customerhomepage(self.driver)

    def clickExitSecurity_fromAdmin(self):
        from Pages.homepage import homepage
        self.action_click(self.exitsecurity)
        return homepage(self.driver)

    def verifyNotAllowed(self):
        self.action_is_visible(self.notAllowed)