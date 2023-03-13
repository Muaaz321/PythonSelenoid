import allure
import pytest
from Tests.controller import controller
from Pages.loginpage import loginpage
from Tests.conftest import USERNAME, PASSWORD


@allure.severity(allure.severity_level.NORMAL)
class Test_Home(controller):

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.title('verifying the title that exist')
    @pytest.mark.skip
    def test_verify_title(self):
        self.loginPage = loginpage(self.driver)
        homePage = self.loginPage.login(USERNAME, PASSWORD)
        title = homePage.get_title("XunisonAdmin")
        assert title == "XunisonAdmin"


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('verifying the gateway search bar exist')
    @pytest.mark.skip
    def test_verify_gatewaysearch(self):
        self.loginPage = loginpage(self.driver)
        homePage = self.loginPage.login(USERNAME, PASSWORD)
        assert homePage.is_search_gateway_exist()
