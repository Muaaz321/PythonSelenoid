import allure
import pytest

from Tests.controller import controller
from Tests.conftest import USERNAME, PASSWORD


@allure.severity(allure.severity_level.NORMAL)
class Test_Login(controller):

    @allure.severity(allure.severity_level.MINOR)
    @allure.title('verifying registration link is exist')
    @pytest.mark.skip
    def test_Register_button_visible(self):
        from Pages.loginpage import loginpage
        self.loginpage = loginpage(self.driver)
        flag = self.loginpage.is_register_button_visible()
        assert flag


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('verifying whether admin can login to the XCPEM')
    @pytest.mark.skip
    def test_login(self):
        from Pages.loginpage import loginpage
        self.loginpage = loginpage(self.driver)
        title = self.loginpage.action_get_title("XunisonAdmin")
        assert title == "XunisonAdmin"
        self.loginpage.setUsername(USERNAME)
        self.loginpage.setPassword(PASSWORD)
        self.loginpage.clickLogin()




