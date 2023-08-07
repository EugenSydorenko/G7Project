from datetime import datetime

from tests.base_test import BaseTest


class LoginPageTest(BaseTest):

    def test_valid_login(self):
        self.login_page.open_login_page()
        self.login_page.enter_text_into_login_field(self.valid_user_email)
        self.login_page.enter_text_into_password_field(self.user_password)
        self.login_page.click_on_button_login()

        assert self.dashboard_page.is_button_log_out_displayed(), 'Button is not displayed'

    def test_new_user_sign_up(self):
        self.login_page.open_login_page()
        self.login_page.click_on_sign_up_button()

        # ToDo:check if this method works
        self.login_page.click_on_account_type_individual()
        self.login_page.click_on_button_get_started()

        self.new_user_signup_page.enter_into_user_first_name_field('Auto')
        self.new_user_signup_page.enter_into_user_last_name_field('Tester')
        self.new_user_signup_page.enter_into_user_name_field('Autotest')
        self.new_user_signup_page.enter_into_user_email_field(self.user_email)
        self.new_user_signup_page.enter_into_user_password_field(self.user_password)
        self.new_user_signup_page.enter_into_user_confirm_password(self.user_password)
        self.new_user_signup_page.click_on_button_sign_up()

        assert self.login_page.is_email_verification_message_displayed(), 'Message is not displayed'

    def test_new_node_deploying(self):
        current_date_time = datetime.now()
        current_date_time = current_date_time.strftime('%Y-%m-%d %H:%M:%S')

        self.login_page.open_login_page()
        self.login_page.enter_text_into_login_field(self.valid_user_email)
        self.login_page.enter_text_into_password_field(self.user_password)
        self.login_page.click_on_button_login()

        self.dashboard_page.click_on_button_add_node()
        self.marketplace_page.click_on_solana_node_deploy_now()

        # ToDo: add waiting for node location to appear

        self.node_deployment_page.click_on_button_deploy_now()
        self.node_deployment_page.enter_node_name_into_node_name_field(current_date_time)
        self.node_deployment_page.enter_ssh_key_into_ssh_key_field(self.test_ssh_key)

        # self.node_deployment_page.enter_promo_code_into_promo_code_field(self.promo_code)

        self.node_deployment_page.click_terms_and_conditions_checkbox()
        # ToDo: add checking if promo code worked
        self.node_deployment_page.click_on_button_proceed()

        # ToDo: check if price is correct
        # ToDo: click on proceed payment
        # ToDo: wait for deployment to finish
        # ToDo: check for successful deployment

        # Add the rest of the test steps related to node buying here
        assert True

    # ToDo: think about different types of nodes and agent checkup


    # agent api tests
    # https://edgevana.atlassian.net/wiki/spaces/ETD/pages/438992897/Proposal+for+Transitioning+to+Microservices+Architecture#Agent.1