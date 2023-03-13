from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from Core.useraction import useraction


load_dotenv()

# print(os.getenv('password'))
# print(sys.path[0])
# print(BROWSER)
# print(USERNAME , PASSWORD , BASEURL)

# def test():
#     conftest.load_locators()
#     locaty = conftest.load_locators["Loginpage"]["username_txt_box"]
#     print(locaty)
#
#
# test()

# userac = useraction(None)
#
#
# user_name = (By.XPATH, userac.locators["Homepage"]["user_name"])
# gateway_search = (By.XPATH, userac.locators["Homepage"]["gateway_search"])
#
# username = (By.XPATH,useraction.locators["Homepage"]["username"])
# print(username)

# print(user_name)
# print(gateway_search)

import subprocess

networks = subprocess.check_output(['netsh', 'wlan', 'show', 'networks']).decode()

ssid_list = []
for line in networks.split('\n'):
    if 'SSID' in line:
        ssid_list.append(line.split(':')[1].strip())


print(ssid_list)

selected_network = input("Twixia3-50G")

subprocess.run(['netsh', 'wlan', 'connect', 'name=' + selected_network])