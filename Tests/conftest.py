import os
import allure
import pytest
from selenium import webdriver
from dotenv import load_dotenv
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

load_dotenv()

BROWSER = os.getenv("browser")
BASEURL = os.getenv("baseUrl")
USERNAME = os.getenv("name")
PASSWORD = os.getenv("password")
WAIT = os.getenv("wait")
REMOTE = os.getenv("selenoidRemote")
VERSION = os.getenv("version")
RUNENV = os.getenv("runenv")
GATEWAY = os.getenv("gateway")
ADMINUSERNAME = os.getenv("adminname")
ADMINPASSWORD = os.getenv("adminpassword")
MESHROLE = os.getenv("meshrole")
FWVERSION = os.getenv("fwversion")
WANMAC = os.getenv("wanmac")



locator_data = None
def configure():

    global BROWSER
    global BASEURL
    global USERNAME
    global PASSWORD
    global WAIT
    global REMOTE
    global VERSION
    global RUNENV
    global GATEWAY
    global ADMINUSERNAME
    global ADMINPASSWORD
    global MESHROLE
    global FWVERSION
    global WANMAC


capabilities = {
        "browserName": "chrome",
        "browserVersion": "109.0",
        "selenoid:options": {
            "enableVideo": False,
            "enableVNC": True
        }
    }


@allure.title('Open XCPEM and check ' + BROWSER + " -- " + VERSION)
@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    driver = None
    browser = os.environ.get("BROWSER")

    if RUNENV.lower() == 'local':
        browser = os.environ.get("BROWSER")
        if browser == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()
        elif browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            driver.maximize_window()
        else:
            raise Exception("Unsupported browser")
    elif RUNENV.lower() == 'remote':
        if browser == "chrome":
            # browser = "chrome"
            options = webdriver.ChromeOptions()
            options.set_capability("browserName", browser)
            options.set_capability("browserVersion", os.environ.get("VERSION"))
            options.set_capability("selenoid:options",
                               {"screenResolution": "1920x1080", "enableVNC": True, "enableVideo": False})
            driver = webdriver.Remote(command_executor=REMOTE, options=options)
            driver.maximize_window()
        elif browser == "firefox":
            # browser = "firefox"
            options = webdriver.FirefoxOptions()
            options.set_capability("browserName", browser)
            options.set_capability("browserVersion", os.environ.get("VERSION"))
            options.set_capability("selenoid:options",
                                   {"screenResolution": "1920x1080", "enableVNC": True, "enableVideo": False})
            driver = webdriver.Remote(command_executor=REMOTE, options=options)
            driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.quit()
    # driver.close()


"""TODO"""
# def load_locators():
#     global locator_data
#     with open(sys.path[0] + "/ObjectRepository/Locators.yaml", "r") as file:
#         locator_data = yaml.safe_load(file)


