from datetime import datetime
import os
import sys

import allure
import yaml
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

from Tests.conftest import WAIT

"""this is parent for all pages"""
"""consist of generic user actions"""
"""load yaml file"""


class useraction:

    with open(sys.path[0] + "/ObjectRepository/Locators.yaml", "r") as file:
        locators = yaml.safe_load(file)
    def __init__(self,driver):
        self.driver = driver

        # with open(sys.path[0] + "/ObjectRepository/Locators.yaml", "r") as file:
        #     locators = yaml.safe_load(file)

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder = "screenshots/{}".format(now)

    def action_click(self,by_locator):
        try:
            WebDriverWait(self.driver,WAIT).until(EC.visibility_of_element_located(by_locator)).click()
        except:
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
                # save screenshot with current timestamp
            screenshot = "{}/error_button_{}.png".format(self.folder, self.now)
            forallure = self.driver.get_screenshot_as_png()
            self.driver.save_screenshot(screenshot)
            allure.attach(forallure,name="screenshot",attachment_type=allure.attachment_type.PNG)
            assert False

    def scroll_down(self,pixels):
        try:
            self.driver.execute_script("window.scrollBy(0, 1000);")
        except:
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
                # save screenshot with current timestamp
            screenshot = "{}/error_button_{}.png".format(self.folder, self.now)
            forallure = self.driver.get_screenshot_as_png()
            self.driver.save_screenshot(screenshot)
            allure.attach(forallure,name="screenshot",attachment_type=allure.attachment_type.PNG)
            assert False


    def switchTonewwindow(self,by_locator):
        try:
            print(" i m in the switch method +++++++++++++++++++")
            WebDriverWait(self.driver, WAIT).until(EC.visibility_of_element_located(by_locator))
            """get the current window handle"""
            current_handle = self.driver.current_window_handle
            """get all the window handles"""
            handles = self.driver.window_handles
            print("Current Handle ----- " + current_handle + "All Handle ----- " + handles)
            """ switch to new window """
            for handle in handles:
                if handle !=current_handle:
                    self.driver.switch_to.window(handle)
                    break
        except:
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
                # save screenshot with current timestamp
            screenshot = "{}/error_button_{}.png".format(self.folder, self.now)
            forallure = self.driver.get_screenshot_as_png()
            self.driver.save_screenshot(screenshot)
            allure.attach(forallure,name="screenshot",attachment_type=allure.attachment_type.PNG)
            assert False

    def action_send_keys(self,by_locator,value):
        try:
            WebDriverWait(self.driver, WAIT).until(EC.visibility_of_element_located(by_locator)).clear()
            WebDriverWait(self.driver,WAIT).until(EC.visibility_of_element_located(by_locator)).send_keys(value)
        except:
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
                # save screenshot with current timestamp
            screenshot = "{}/error_textbox_{}.png".format(self.folder, self.now)
            forallure = self.driver.get_screenshot_as_png()
            self.driver.save_screenshot(screenshot)
            allure.attach(forallure, name="screenshot", attachment_type=allure.attachment_type.PNG)
            assert False
    def action_get_text(self,by_locator):
        try:
            element = WebDriverWait(self.driver,WAIT).until(EC.visibility_of_element_located(by_locator))
            print(element.text + "   ______________________________")
            return element.text
        except:
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
                # save screenshot with current timestamp
            screenshot = "{}/error_gettext_{}.png".format(self.folder, self.now)
            forallure = self.driver.get_screenshot_as_png()
            self.driver.save_screenshot(screenshot)
            allure.attach(forallure, name="screenshot", attachment_type=allure.attachment_type.PNG)
            assert False

    def action_is_visible(self,by_locator):
        try:
            element = WebDriverWait(self.driver,WAIT).until((EC.visibility_of_element_located(by_locator)))
            return bool(element)
        except:
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
                # save screenshot with current timestamp
            screenshot = "{}/error_isvisible_{}.png".format(self.folder, self.now)
            forallure = self.driver.get_screenshot_as_png()
            self.driver.save_screenshot(screenshot)
            allure.attach(forallure, name="screenshot", attachment_type=allure.attachment_type.PNG)
            assert False

    def action_get_title(self,title):
        try:
            WebDriverWait(self.driver,WAIT).until(EC.title_is(title))
            return self.driver.title
        except:
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
                # save screenshot with current timestamp
            screenshot = "{}/error_gettitle_{}.png".format(self.folder, self.now)
            forallure = self.driver.get_screenshot_as_png()
            self.driver.save_screenshot(screenshot)
            allure.attach(forallure, name="screenshot", attachment_type=allure.attachment_type.PNG)
            assert False


