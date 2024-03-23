import allure
from pages.main_page import main_page
from test_data.user_data import VALID_CREDENTIALS, INVALID_CREDENTIALS


class TestAuthorization:

    @allure.title("Successful authorization") # коммент для теста
    def test_authorization_successful(self, browser_management):
        with allure.step("Open main page"):
            main_page.open_main_page()
        with allure.step("Open authorization page"):
            main_page.open_authorization_page()
        with allure.step("Enter the correct login"):
            main_page.fill_login(VALID_CREDENTIALS.login)
        with allure.step("Click on the continue button"):
            main_page.click_button_continue()
        with allure.step("Enter the correct password"):
            main_page.fill_password(VALID_CREDENTIALS.password)
        with allure.step("Click on the login button"):
            main_page.click_button_enter()
        with allure.step("Close pop-up window"):
            main_page.close_number_pop_up()
        with allure.step("Open profile"):
            main_page.open_profile()
        with allure.step("Verifying successful authorization"):
            main_page.should_authorization_success()

    @allure.title("Unsuccessful authorization")
    def test_authorization_failed(self, browser_management):
        with allure.step("Open main page"):
            main_page.open_main_page()
        with allure.step("Open authorization page"):
            main_page.open_authorization_page()
        with allure.step("Enter the correct login"):
            main_page.fill_login(VALID_CREDENTIALS.login)
        with allure.step("Click on the continue button"):
            main_page.click_button_continue()
        with allure.step("Enter the fake password"):
            main_page.fill_fake_password(INVALID_CREDENTIALS.password)
        with allure.step("Click on the login button"):
            main_page.click_button_enter()
        with allure.step("Checking failed authorization"):
            main_page.should_validation_massage()
