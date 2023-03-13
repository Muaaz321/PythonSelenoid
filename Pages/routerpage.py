import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Core.useraction import useraction
from Pages.securitypage import securitypage


class routerpage(useraction):

    def __init__(self, driver):
        super().__init__(driver)

    userac = useraction(None)

    security_platform = (By.XPATH,userac.locators["Routerpage"]["security_platform"])
    smarthome_platform = (By.XPATH, userac.locators["Routerpage"]["security_platform"])
    router_platform = (By.XPATH, userac.locators["Routerpage"]["security_platform"])
    requestcyber_logs = (By.XPATH, userac.locators["Routerpage"]["security_platform"])
    device_info = (By.XPATH,"//p[contains(text(),'Services')]")


    def get_title(self,title):
        return self.action_get_title(title)

    def clickSecurityplatform(self):
        self.action_click(self.security_platform)
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[2])
        return securitypage(self.driver)

    def scroll_down(self,pixels):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.execute_script("window.scrollBy(0, "+str(pixels)+");")

    def goDown(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.execute_script("window.scrollBy(0,1000)","")
        # self.driver.execute_script("argument[0].scrollIntoView();", self.device_info)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def clickDeviceService(self):
        self.action_click(self.device_info)
        time.sleep(5)








