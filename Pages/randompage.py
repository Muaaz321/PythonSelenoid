import os
import time

import allure
from _pytest import assertion
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Core.useraction import useraction
from bs4 import BeautifulSoup

from Tests.conftest import WAIT


class randompage(useraction):

    def __init__(self,driver):
        super().__init__(driver)

    userac = useraction(None)

    googlesearchbox = (By.XPATH,userac.locators["Randompage"]["googlesearchbox"])
    parenalcontroltemplate = (By.XPATH,userac.locators["Randompage"]["parentalcontrol_template"])
    topAdvertistment = (By.XPATH,"//iframe[@title='3rd party ad content' and @data-google-container-id='1']")
    sideAdvertistment = (By.XPATH,"//iframe[@title='3rd party ad content' and @data-google-container-id='4']")


    """Page actions """
    def verifyfromgoogle(self,searchpara):
        self.driver.get("https://www.google.com/")
        self.action_send_keys(self.googlesearchbox,searchpara)
        WebDriverWait(self.driver,WAIT).until(EC.visibility_of_element_located(self.googlesearchbox)).send_keys(Keys.RETURN)

        time.sleep(10)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        html = self.driver.page_source
        soup = BeautifulSoup(html,"html.parser")

        # Assert that the text "porno.com" is not in the page
        try:
            assert "pornhub.com" not in soup.get_text(), "The text 'pornhub.com' was found on the page -GOOGLE"
        except AssertionError as e:
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
                # save screenshot with current timestamp
            screenshot = "{}/error_button_{}.png".format(self.folder, self.now)
            forallure = self.driver.get_screenshot_as_png()
            self.driver.save_screenshot(screenshot)
            allure.attach(forallure, name="screenshot", attachment_type=allure.attachment_type.PNG)
            assert False

    def verifyfrombing(self, searchpara):
        self.driver.get("https://www.bing.com/")
        self.action_send_keys(self.googlesearchbox, searchpara)
        WebDriverWait(self.driver,WAIT).until(EC.visibility_of_element_located(self.googlesearchbox)).send_keys(Keys.RETURN)

        time.sleep(10)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        # Assert that the text "porno.com" is not in the page
        try:
            assert "pornhub.com" not in soup.get_text(), "The text 'pornhub.com' was found on the page - BING"
        except AssertionError as e:
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
                # save screenshot with current timestamp
            screenshot = "{}/error_button_{}.png".format(self.folder, self.now)
            forallure = self.driver.get_screenshot_as_png()
            self.driver.save_screenshot(screenshot)
            allure.attach(forallure, name="screenshot", attachment_type=allure.attachment_type.PNG)
            assert False
    def verifyfromsite(self, website):
        url = self.driver.get("https://www."+website+".com/")

        try:
            self.driver.get(url)
            sitetitle = self.driver.title
            assert sitetitle != "Porno Movies & Free XXX Porn Videos"
        except AssertionError as e:
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
                # save screenshot with current timestamp
            screenshot = "{}/error_button_{}.png".format(self.folder, self.now)
            forallure = self.driver.get_screenshot_as_png()
            self.driver.save_screenshot(screenshot)
            allure.attach(forallure, name="screenshot", attachment_type=allure.attachment_type.PNG)
            assert False



    def verifyfromsite_shouldableto(self, website):
        url = "https://www." + website + ".com/"
        self.driver.get(url)
        try:
            sitetitle = self.driver.title
            print(sitetitle + " from the site ++++++++++++++++++++++++++++++++ ")
            assert sitetitle == "Porno Movies & Free XXX Porn Videos"
        except AssertionError as e:
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
                # save screenshot with current timestamp
            screenshot = "{}/error_button_{}.png".format(self.folder, self.now)
            forallure = self.driver.get_screenshot_as_png()
            self.driver.save_screenshot(screenshot)
            allure.attach(forallure, name="screenshot", attachment_type=allure.attachment_type.PNG)
            assert False

    def verifyfromcrizbuzz(self):
        url = self.driver.get("https://www.cricbuzz.com/")
        element = self.topAdvertistment
        element2 = self.sideAdvertistment

        wait = WebDriverWait(self.driver, WAIT)
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        try:
            assert element is not None
            assert element2 is not None
        except AssertionError as e:
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
                # save screenshot with current timestamp
            screenshot = "{}/error_button_{}.png".format(self.folder, self.now)
            forallure = self.driver.get_screenshot_as_png()
            self.driver.save_screenshot(screenshot)
            allure.attach(forallure, name="screenshot", attachment_type=allure.attachment_type.PNG)
            print(e)
            assert False


    def verifyfromcrizbuzz_noadvertistment(self):
        url = self.driver.get("https://www.cricbuzz.com/")

        element = self.topAdvertistment
        element2 = self.sideAdvertistment

        wait = WebDriverWait(self.driver, WAIT)
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        try:
            assert not element, "Top advertisement exists"
            assert not element2, "Side advertisement exists"
        except AssertionError as e:
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
                # save screenshot with current timestamp
            screenshot = "{}/error_button_{}.png".format(self.folder, self.now)
            forallure = self.driver.get_screenshot_as_png()
            self.driver.save_screenshot(screenshot)
            allure.attach(forallure, name="screenshot", attachment_type=allure.attachment_type.PNG)
            print(e.args[0])
            assert False


