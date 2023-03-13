import time
import unittest

import allure
import pytest
import softest as softest
from selenium.webdriver.common.by import By

from Tests.controller import controller
from Core.useraction import useraction
from Core.utility import utility
from Tests.conftest import USERNAME, PASSWORD, WAIT, ADMINUSERNAME, ADMINPASSWORD, GATEWAY, MESHROLE, FWVERSION, WANMAC
from ObjectRepository.Constant import familyshieldxpath, abblockerxpath, safesearchxpath, delay, meshrolexpath, \
    firmwarexpath, wanmacxpath, gatewayxpath, provisionxpath, routerstatusxpath, ltemodulexpath, parentalcontrolxpath


@allure.severity(allure.severity_level.BLOCKER)
class Test_Smoke(controller):

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.title('7603 - Setting ON, OFF values for all Family Shield status mode as User')
    @pytest.mark.skip
    def test_setonoff_securityoptions1(self):
        from Pages.loginpage import loginpage
        self.loginpage = loginpage(self.driver)
        title = self.loginpage.action_get_title("XunisonAdmin")
        assert title == "XunisonAdmin"

        """ Login from customer"""
        self.loginpage.setUsername(USERNAME)
        self.loginpage.setPassword(PASSWORD)
        self.loginpage.clickLogin()

        customerHomePage = self.loginpage.clickGateway()
        securityPage = customerHomePage.clickSecurity()

        time.sleep(20)

        """ Retrieve status before the change """
        get_statuses = lambda xpaths: [useraction.action_get_text(self, (By.XPATH, xpath)) for xpath in xpaths]
        family_shield, ad_blocker, safe_search = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])


        """ making safeSearch familyshield adblocker OFF as precondition """
        if family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'OFF':
            pass
        elif family_shield == 'ON' and ad_blocker == 'ON' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and safe_search == "OFF" and ad_blocker == 'ON':
            securityPage.clickAdblockerphishing()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'ON':
            securityPage.clickSafesearch()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'ON' and safe_search == 'ON':
            securityPage.clickAdblockerphishing()
            time.sleep(delay)
            securityPage.clickSafesearch()
            time.sleep(delay)

        """"Retrieve status after the change """
        familyshield, adblock, safesearch = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ 2.1 verification """
        assert familyshield == 'OFF'
        assert adblock == 'OFF'
        assert safesearch == 'OFF'

        securityPage.clickFamilyshield()
        time.sleep(delay)

        """"Retrieve status after the change """
        familyshield2, adblock2, safesearch2 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ 3.1 verification """
        assert familyshield2 == 'ON'
        assert adblock2 == 'ON'
        assert safesearch2 == 'ON'

        securityPage.clickAdblockerphishing()
        time.sleep(delay)

        """"Retrieve status after the change """
        familyshield3, adblock3, safesearch3 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ 4.1 verification """
        assert familyshield3 == 'OFF'
        assert adblock3 == 'OFF'
        assert safesearch3 == 'ON'

        securityPage.clickAdblockerphishing()
        time.sleep(delay)

        """"Retrieve status after the change """
        familyshield4, adblock4, safesearch4 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ 5.1 verification """
        assert familyshield4 == 'OFF'
        assert adblock4 == 'ON'
        assert safesearch4 == 'ON'

        securityPage.clickFamilyshield()
        time.sleep(delay)

        """ Turn OFF safesearch """
        securityPage.clickSafesearch()
        time.sleep(delay)

        """"Retrieve status after the change """
        familyshield5, adblock5, safesearch5 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ 7.1 verification """
        assert familyshield5 == 'OFF'
        assert adblock5 == 'ON'
        assert safesearch5 == 'OFF'

        """ Turn ON safesearch """
        securityPage.clickSafesearch()
        time.sleep(delay)

        """"Retrieve status after the change """
        familyshield6, adblock6, safesearch6 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ 8.1 verification """
        assert familyshield6 == 'OFF'
        assert adblock6 == 'ON'
        assert safesearch6 == 'ON'

        """Log out from Customer"""
        customerHomePage = securityPage.clickExitSecurity()
        customerHomePage.clickLogout()


    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.title('7604 - Setting ON, OFF values for Ad Block, Safe Search mode as Admin')
    @pytest.mark.skip
    def test_setonoff_securityoptions4(self): # Have to run in US.DEV this will not work in XU
        from Pages.loginpage import loginpage
        self.loginpage = loginpage(self.driver)
        title = self.loginpage.action_get_title("XunisonAdmin")
        assert title == "XunisonAdmin"

        """ Login as Admin """""
        self.loginpage.setUsername("admin@xunison.com")
        self.loginpage.setPassword("Xunison123")
        self.loginpage.clickLogin()

        customerHomePage = self.loginpage.clickGateway()
        securityPage = customerHomePage.clickSecurity()

        time.sleep(20)

        get_statuses = lambda xpaths: [useraction.action_get_text(self, (By.XPATH, xpath)) for xpath in xpaths]
        family_shield, ad_blocker, safe_search = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ making safeSearch familyshield adblocker ON as precondition """
        if family_shield == 'ON' and ad_blocker == 'ON' and safe_search == 'ON':
            pass
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'OFF':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and safe_search == "OFF" and ad_blocker == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'ON' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)

        """turn OFF safe search"""
        securityPage.clickSafesearch()
        time.sleep(delay)

        """"Retrieve status after the change """
        familyshield1, adblock1, safesearch1 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ 2.1 verification """
        assert familyshield1 == 'OFF'
        assert adblock1 == 'ON'
        assert safesearch1 == 'OFF'

        """turn ON safe search"""
        securityPage.clickSafesearch()
        assert securityPage.notAllowed

        """"Retrieve status after the change """
        familyshield2, adblock2, safesearch2 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ 3.2 verification """
        assert familyshield2 == 'OFF'
        assert adblock2 == 'ON'
        assert safesearch2 == 'OFF'

        """turn OFF adblock"""
        securityPage.clickAdblockerphishing()
        time.sleep(delay)

        """"Retrieve status after the change """
        familyshield3, adblock3, safesearch3 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ 4.1 verification - allure has mistaken"""
        assert familyshield3 == 'OFF'
        assert adblock3 == 'OFF'
        assert safesearch3 == 'OFF'

        """turn ON adblock"""
        securityPage.clickAdblockerphishing()
        assert securityPage.notAllowed
        time.sleep(delay)

        """"Retrieve status after the change """
        familyshield4, adblock4, safesearch4 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ 4.1 verification - allure has mistaken"""
        assert familyshield4 == 'OFF'
        assert adblock4 == 'OFF'
        assert safesearch4 == 'OFF'

        """ Log out from the Admin """
        adminHomepage = securityPage.clickExitSecurity_fromAdmin()
        loginpage = adminHomepage.clickLogout()

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.title('7605 - Setting ON, OFF values for Family Shield mode as Admin')
    @pytest.mark.skip
    def test_setonoff_securityoptions9(self):
        from Pages.loginpage import loginpage
        self.loginpage = loginpage(self.driver)
        title = self.loginpage.action_get_title("XunisonAdmin")
        assert title == "XunisonAdmin"

        """Verify safe search is turn on Customer Panel"""
        """ making safeSearch ON through customer as precondition """
        self.loginpage.setUsername(USERNAME)
        self.loginpage.setPassword(PASSWORD)
        self.loginpage.clickLogin()

        customerHomePage = self.loginpage.clickGateway()
        securityPage = customerHomePage.clickSecurity()

        time.sleep(20)

        get_statuses = lambda xpaths: [useraction.action_get_text(self, (By.XPATH, xpath)) for xpath in xpaths]
        family_shield, ad_blocker, safe_search = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ making safeSearch familyshield adblocker ON as precondition """
        if family_shield == 'ON' and ad_blocker == 'ON' and safe_search == 'ON':
            pass
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'OFF':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and safe_search == "OFF" and ad_blocker == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'ON' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)

        print(family_shield + ad_blocker + safe_search + "All Status ")

        """ Log out from the Customer """
        customerHomePage = securityPage.clickExitSecurity()
        customerHomePage.clickLogout()

        """ Login as Admin """
        Homepage = self.loginpage.login("muaaz+admin@xunison.com", "Admin123456")
        Homepage.search_gateway("bb82a2ce6cfe4fcba1a42cc9945da671")
        time.sleep(delay)
        Homepage.navigate_to_onlinedevice()
        """ remember to change the xpath"""
        time.sleep(delay)
        Routerpage = Homepage.clickGatewayrecord("bb82a2ce6cfe4fcba1a42cc9945da671")
        Securitypage = Routerpage.clickSecurityplatform()
        time.sleep(delay)
        #
        get_statuses = lambda xpaths: [useraction.action_get_text(self, (By.XPATH, xpath)) for xpath in xpaths]
        family_shield1, ad_blocker1, safe_search1 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ making Family sheild OFF """
        if (safe_search1 == 'ON'):
            Securitypage.clickFamilyshield()
            time.sleep(delay)
        else:
            print("Invalid state for ad block should be OFF but it is " + ad_blocker1)
        #
        familyshield2, adblock2, safesearch2 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])
        print(familyshield2 + adblock2 + safesearch2 + "status >>>>>>>>> ")

        """4.1 Verification point"""
        assert familyshield2 == 'OFF'
        assert adblock2 == 'OFF'
        assert safesearch2 == 'OFF'

        """ try to make Family shield ON"""
        Securitypage.clickFamilyshield()
        assert Securitypage.notAllowed

        adminHomepage = Securitypage.clickExitSecurity_fromAdmin()
        loginpage = adminHomepage.clickLogout()

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.title('7606 - Setting ON, OFF values for Ad Block ,Safe Search mode as Support')
    @pytest.mark.skip
    def test_setonoff_securityoptionsdelay(self):
        from Pages.loginpage import loginpage
        self.loginpage = loginpage(self.driver)
        title = self.loginpage.action_get_title("XunisonAdmin")
        assert title == "XunisonAdmin"

        """Verify safe search is turn on Customer Panel"""
        """ making safeSearch ON through customer as precondition """
        self.loginpage.setUsername(USERNAME)
        self.loginpage.setPassword(PASSWORD)
        self.loginpage.clickLogin()

        customerHomePage = self.loginpage.clickGateway()
        securityPage = customerHomePage.clickSecurity()

        time.sleep(20)

        get_statuses = lambda xpaths: [useraction.action_get_text(self, (By.XPATH, xpath)) for xpath in xpaths]
        family_shield, ad_blocker, safe_search = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ making safeSearch familyshield adblocker ON as precondition """
        if family_shield == 'ON' and ad_blocker == 'ON' and safe_search == 'ON':
            pass
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'OFF':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and safe_search == "OFF" and ad_blocker == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'ON' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)

        """ Log out from the Customer """
        customerHomePage = securityPage.clickExitSecurity()
        customerHomePage.clickLogout()

        """ Login as Support """
        SupportPage = self.loginpage.login_support("muaaz+support@xunison.com", "Support123456")
        Homepage = SupportPage.search_gatewayemail(USERNAME)
        time.sleep(delay)
        Homepage.navigate_to_onlinedevice()
        # """ remember to change the xpath"""
        time.sleep(delay)
        Routerpage = Homepage.clickGatewayrecord("bb82a2ce6cfe4fcba1a42cc9945da671")
        Securitypage = Routerpage.clickSecurityplatform()
        time.sleep(delay)

        et_statuses = lambda xpaths: [useraction.action_get_text(self, (By.XPATH, xpath)) for xpath in xpaths]
        family_shield1, ad_blocker1, safe_search1 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ making safe search OFF """
        if (safe_search1 == 'ON'):
            Securitypage.clickSafesearch()
            time.sleep(delay)
        else:
            print("Invalid state for Safe search should be OFF but it is " + safe_search1)

        familyshield2, adblock2, safesearch2 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])
        print(familyshield2 + adblock2 + safesearch2 + "status >>>>>>>>> ")

        """2.1 Verification point"""
        assert familyshield2 == 'OFF'
        assert adblock2 == 'ON'
        assert safesearch2 == 'OFF'

        """ 3.2 try to make Safe Search ON"""
        Securitypage.clickSafesearch()
        assert Securitypage.notAllowed

        """ try to ad block Off"""
        Securitypage.clickAdblockerphishing()
        time.sleep(delay)

        familyshield3, adblock3, safesearch3 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])
        print(familyshield3 + adblock3 + safesearch3 + "status >>>>>>>>> ")

        """4.1 Verification point"""
        assert familyshield3 == 'OFF'
        assert adblock3 == 'OFF'
        assert safesearch3 == 'OFF'

        """ 5.1 try to ad block ON"""
        Securitypage.clickAdblockerphishing()
        assert Securitypage.notAllowed

        adminHomepage = Securitypage.clickExitSecurity_fromAdmin()
        loginpage = adminHomepage.clickLogout()


    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.title('7607 - Setting ON, OFF values for Family Shield mode as Support')
    @pytest.mark.skip
    def test_setonoff_securityoptions11(self):
        from Pages.loginpage import loginpage
        self.loginpage = loginpage(self.driver)
        title = self.loginpage.action_get_title("XunisonAdmin")
        assert title == "XunisonAdmin"

        """ Login as Customer """
        self.loginpage.setUsername(USERNAME)
        self.loginpage.setPassword(PASSWORD)
        self.loginpage.clickLogin()

        customerHomePage = self.loginpage.clickGateway()
        securityPage = customerHomePage.clickSecurity()

        time.sleep(20)

        get_statuses = lambda xpaths: [useraction.action_get_text(self, (By.XPATH, xpath)) for xpath in xpaths]
        family_shield, ad_blocker, safe_search = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ making safeSearch familyshield adblocker ON as precondition """
        if family_shield == 'ON' and ad_blocker == 'ON' and safe_search == 'ON':
            pass
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'OFF':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and safe_search == "OFF" and ad_blocker == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'ON' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)

        """ Log out from the Customer """
        customerHomePage = securityPage.clickExitSecurity()
        customerHomePage.clickLogout()

        """ Login as Support """
        SupportPage = self.loginpage.login_support("muaaz+support@xunison.com", "Support123456")
        Homepage = SupportPage.search_gatewayemail(USERNAME)
        time.sleep(delay)
        Homepage.navigate_to_onlinedevice()
        # """ remember to change the xpath"""
        time.sleep(delay)
        Routerpage = Homepage.clickGatewayrecord("bb82a2ce6cfe4fcba1a42cc9945da671")
        Securitypage = Routerpage.clickSecurityplatform()
        time.sleep(delay)

        et_statuses = lambda xpaths: [useraction.action_get_text(self, (By.XPATH, xpath)) for xpath in xpaths]
        family_shield1, ad_blocker1, safe_search1 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ making family sheild OFF """
        if (family_shield1 == 'ON'):
            Securitypage.clickFamilyshield()
            time.sleep(delay)
        else:
            print("Invalid state for Family shield should be OFF but it is " + family_shield1)

        familyshield2, adblock2, safesearch2 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])
        print(familyshield2 + adblock2 + safesearch2 + "status >>>>>>>>> ")

        """2.1 Verification point"""
        assert familyshield2 == 'OFF'
        assert adblock2 == 'OFF'
        assert safesearch2 == 'OFF'

        """ 3 try to make Family Shield ON"""
        Securitypage.clickFamilyshield()
        assert Securitypage.notAllowed

        familyshield3, adblock3, safesearch3 = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])
        print(familyshield3 + adblock3 + safesearch3 + "status >>>>>>>>> ")

        """3.2 Verification point"""
        assert familyshield3 == 'OFF'
        assert adblock3 == 'OFF'
        assert safesearch3 == 'OFF'

        adminHomepage = Securitypage.clickExitSecurity_fromAdmin()
        loginpage = adminHomepage.clickLogout()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('7608 - Block to content 18+ in the search and navigation via direct link')
    @pytest.mark.skip
    def test_setonoff_securityoptions12(self):
        from Pages.loginpage import loginpage
        from Pages.randompage import randompage

        self.loginpage = loginpage(self.driver)
        title = self.loginpage.action_get_title("XunisonAdmin")
        assert title == "XunisonAdmin"

        """Verify safe search is turn on Customer Panel"""
        """ making safeSearch ON through customer as precondition """
        self.loginpage.setUsername("muaaz.mohideen+1@xunison.com")
        self.loginpage.setPassword("Allblacks123")
        self.loginpage.clickLogin()

        customerHomePage = self.loginpage.clickGateway()
        securityPage = customerHomePage.clickSecurity()

        time.sleep(delay)

        get_statuses = lambda xpaths: [useraction.action_get_text(self, (By.XPATH, xpath)) for xpath in xpaths]
        family_shield, ad_blocker, safe_search = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        print(familyshieldxpath + abblockerxpath + safesearchxpath + "All Status ")

        """ making safeSearch familyshield adblocker ON as precondition """
        if family_shield == 'ON' and ad_blocker == 'ON' and safe_search == 'ON':
            pass
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'OFF':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and safe_search == "OFF" and ad_blocker == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'ON' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)

        """ Log out from the Customer """
        customerHomePage = securityPage.clickExitSecurity()
        customerHomePage.clickLogout()

        randomwebsearch = randompage(self.driver)
        randomwebsearch.verifyfromgoogle("porn")
        randomwebsearch.verifyfrombing("porn")
        randomwebsearch.verifyfromsite("porno") # have to check

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('7610 delay - Block to content 18+ in the search but unblock via direct link')
    @pytest.mark.skip
    def test_setonoff_securityoptions13(self):
        from Pages.loginpage import loginpage
        from Pages.randompage import randompage

        self.loginpage = loginpage(self.driver)
        title = self.loginpage.action_get_title("XunisonAdmin")
        assert title == "XunisonAdmin"

        """Verify safe search is turn on Customer Panel"""
        """ making safeSearch ON through customer as precondition """
        self.loginpage.setUsername("muaaz.mohideen+1@xunison.com")
        self.loginpage.setPassword("Allblacks123")
        self.loginpage.clickLogin()

        customerHomePage = self.loginpage.clickGateway()
        securityPage = customerHomePage.clickSecurity()

        time.sleep(delay)

        get_statuses = lambda xpaths: [useraction.action_get_text(self, (By.XPATH, xpath)) for xpath in xpaths]
        family_shield, ad_blocker, safe_search = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ making safeSearch familyshield adblocker ON as precondition """
        if family_shield == 'ON' and ad_blocker == 'ON' and safe_search == 'ON':
            pass
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'OFF':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and safe_search == "OFF" and ad_blocker == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'ON' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)

        """turn OFF familyshield"""
        securityPage.clickFamilyshield()
        time.sleep(delay)

        """ turn ON safeSearch """
        securityPage.clickFamilyshield()
        time.sleep(delay)


        """ Log out from the Customer """
        customerHomePage = securityPage.clickExitSecurity()
        customerHomePage.clickLogout()

        randomwebsearch = randompage(self.driver)
        randomwebsearch.verifyfromgoogle("porn")
        randomwebsearch.verifyfrombing("porn")
        randomwebsearch.verifyfromsite_shouldableto("porno") # have to check

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('7611 - Block Ad and cross-site tracking')
    @pytest.mark.skip
    def test_setonoff_securityoptions14(self):
        from Pages.loginpage import loginpage
        from Pages.randompage import randompage

        self.loginpage = loginpage(self.driver)
        title = self.loginpage.action_get_title("XunisonAdmin")
        assert title == "XunisonAdmin"

        """ Customer Login """
        self.loginpage.setUsername("muaaz.mohideen@xunison.com")
        self.loginpage.setPassword("Allblacks123")
        self.loginpage.clickLogin()

        customerHomePage = self.loginpage.clickGateway()
        securityPage = customerHomePage.clickSecurity()

        time.sleep(delay)

        get_statuses = lambda xpaths: [useraction.action_get_text(self, (By.XPATH, xpath)) for xpath in xpaths]
        family_shield, ad_blocker, safe_search = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])


        """ making safeSearch familyshield adblocker OFF as precondition """
        if family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'OFF':
            pass
        elif family_shield == 'ON' and ad_blocker == 'ON' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and safe_search == "OFF" and ad_blocker == 'ON':
            securityPage.clickAdblockerphishing()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'ON':
            securityPage.clickSafesearch()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'ON' and safe_search == 'ON':
            securityPage.clickAdblockerphishing()
            time.sleep(delay)
            securityPage.clickSafesearch()
            time.sleep(delay)

        """turn ON Adblocker"""
        securityPage.clickAdblockerphishing()
        time.sleep(delay)

        """ Log out from the Customer """
        customerHomePage = securityPage.clickExitSecurity()
        customerHomePage.clickLogout()

        randomwebsearch = randompage(self.driver)
        time.sleep(delay)

        """ 1.1 Verification"""
        randomwebsearch.verifyfromcrizbuzz()


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('7612 - Unblock Ad and cross-site tracking')
    @pytest.mark.skip
    def test_setonoff_securityoptions15(self):
        from Pages.loginpage import loginpage
        from Pages.randompage import randompage

        self.loginpage = loginpage(self.driver)
        title = self.loginpage.action_get_title("XunisonAdmin")
        assert title == "XunisonAdmin"

        """ Customer Login """
        self.loginpage.setUsername("muaaz.mohideen@xunison.com")
        self.loginpage.setPassword("Allblacks123")
        self.loginpage.clickLogin()

        customerHomePage = self.loginpage.clickGateway()
        securityPage = customerHomePage.clickSecurity()

        time.sleep(delay)

        get_statuses = lambda xpaths: [useraction.action_get_text(self, (By.XPATH, xpath)) for xpath in xpaths]
        family_shield, ad_blocker, safe_search = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ making safeSearch familyshield adblocker ON as precondition """
        if family_shield == 'ON' and ad_blocker == 'ON' and safe_search == 'ON':
            pass
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'OFF':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and safe_search == "OFF" and ad_blocker == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'ON' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)

        """turn OFF Adblocker"""
        securityPage.clickAdblockerphishing()
        time.sleep(delay)

        """ Log out from the Customer """
        customerHomePage = securityPage.clickExitSecurity()
        customerHomePage.clickLogout()

        randomwebsearch = randompage(self.driver)
        time.sleep(delay)

        """ 1.1 Verification"""
        randomwebsearch.verifyfromcrizbuzz_noadvertistment()


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('7701 Display router information on the Gateway page for Master (Online) as Admin/Support')
    def test_verify_device_info(self):
        from Pages.loginpage import loginpage
        from Pages.randompage import randompage

        self.loginpage = loginpage(self.driver)
        title = self.loginpage.action_get_title("XunisonAdmin")
        assert title == "XunisonAdmin"

        """ Login as Admin """
        Homepage = self.loginpage.login(ADMINUSERNAME, ADMINPASSWORD)
        Homepage.search_gateway(GATEWAY)
        time.sleep(int(WAIT))
        Homepage.navigate_to_onlinedevice()

        Routerpage = Homepage.clickGatewayrecord(GATEWAY)
        Routerpage.clickDeviceService()
        time.sleep(int(WAIT))

        get_device_information = lambda xpaths: [useraction.action_get_text(self, (By.XPATH, xpath)) for xpath in xpaths]
        meshrole, firmware, wanmac , gateway,provision,routerstatus,ltemodule,parentalcontrol = get_device_information(
            [meshrolexpath, firmwarexpath, wanmacxpath,gatewayxpath,provisionxpath,routerstatusxpath,ltemodulexpath,parentalcontrolxpath])

        print(get_device_information)

        # self.soft_assert(self.assertEqual(meshrole,"Maste","meshrol is not equal to Master"))
        # self.soft_assert(self.assertEqual(firmware, "3.2.", "firmware is not equal to 3.2.4"))

        assert meshrole in MESHROLE
        assert firmware in FWVERSION
        assert wanmac in WANMAC
        assert gateway in GATEWAY
        # assert provision in USERNAME
        assert routerstatus in "Online"
        assert ltemodule in "Not installed"
        assert parentalcontrol in "Not Active"


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('7696 - Access to content 18+ for a client device connected to LAN')
    @pytest.mark.skip
    def test_setonoff_securityoptions13(self):
        from Pages.loginpage import loginpage
        from Pages.randompage import randompage

        """ change to LAN network R & D"""
        utility.selectNetwork("Twixia3-35G")

        self.loginpage = loginpage(self.driver)
        title = self.loginpage.action_get_title("XunisonAdmin")
        assert title == "XunisonAdmin"

        """Verify safe search is turn on Customer Panel"""
        """ making safeSearch ON through customer as precondition """
        self.loginpage.setUsername("muaaz.mohideen+1@xunison.com")
        self.loginpage.setPassword("Allblacks123")
        self.loginpage.clickLogin()

        customerHomePage = self.loginpage.clickGateway()
        securityPage = customerHomePage.clickSecurity()

        time.sleep(delay)

        get_statuses = lambda xpaths: [useraction.action_get_text(self, (By.XPATH, xpath)) for xpath in xpaths]
        family_shield, ad_blocker, safe_search = get_statuses(
            [familyshieldxpath, abblockerxpath, safesearchxpath])

        """ making safeSearch familyshield adblocker ON as precondition """
        if family_shield == 'ON' and ad_blocker == 'ON' and safe_search == 'ON':
            pass
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'OFF':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and safe_search == "OFF" and ad_blocker == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'OFF' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)
        elif family_shield == 'OFF' and ad_blocker == 'ON' and safe_search == 'ON':
            securityPage.clickFamilyshield()
            time.sleep(delay)

        """turn OFF familyshield"""
        securityPage.clickFamilyshield()
        time.sleep(delay)

        """ turn ON safeSearch """
        securityPage.clickFamilyshield()
        time.sleep(delay)

        """ Log out from the Customer """
        customerHomePage = securityPage.clickExitSecurity()
        customerHomePage.clickLogout()

        randomwebsearch = randompage(self.driver)
        randomwebsearch.verifyfromgoogle("porn")
        randomwebsearch.verifyfrombing("porn")
        randomwebsearch.verifyfromsite_shouldableto("porno")  # have to check


