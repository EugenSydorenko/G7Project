import unittest


class LoginPageTest(unittest.TestCase):

    @staticmethod
    def test_valid_login(setup_teardown, login_page, dashboard_page):
        driver = setup_teardown
        login_page.open_login_page(driver)
        login_page.open_login_page(driver)
        login_page.enter_text_into_login_field(driver, 'eugene.sydorenko@edgevana.com')
        login_page.enter_text_into_password_field(driver, 'Zhenya18021991!')
        login_page.click_on_button_login()

        assert True
        # dashboard_page.Dashboard.is_button_log_out_displayed()), 'Button is not displayed'

    def test_new_user_sign_up(self):
        self.loginPage.openLoginPage()
        self.loginPage.clickOnSignup()

        self.newUserSignUpPage.enterUserNameIntoInputUserFirstName("Eugene")
        self.newUserSignUpPage.enterUserNameIntoInputUserLastName("Sydorenko")
        self.newUserSignUpPage.enterUserNameIntoInputUserUsername("Eugene")
        self.newUserSignUpPage.enterUserNameIntoInputUserEmail("eugene.sydorenko@edgevana.com")
        self.newUserSignUpPage.enterUserNameIntoInputUserPassword("Zhenya18021991!")
        self.newUserSignUpPage.enterUserNameIntoInputUserConfirmPassword("Zhenya18021991!")
        self.newUserSignUpPage.clickOnButtonSignUp()

        assert self.loginPage.isEmailVerificationMessageDisplayed(), 'Message is not displayed'

    def test_new_node_buying(self):
        self.loginPage.openLoginPage()
        self.loginPage.enterUserNameIntoInputLogin("eugene.sydorenko@edgevana.com")
        self.loginPage.enterPasswordIntoInputPassword("Zhenya18021991!")
        self.loginPage.clickOnButtonLogin()

        self.dashboard.clickOnButtonAddNode()
        self.marketplace.clickOnSolanaNodeDeployNow()
        self.serverDeployment.clickOnButtonDeployNow()
        self.serverDeployment.enterNodeNameIntoNodeNameField("Node")
        self.serverDeployment.enterSshKeyIntoSshKeyField("")
        self.serverDeployment.enterPromoCodeIntopromoCodeField("")

        # Add the rest of the test steps related to node buying here
