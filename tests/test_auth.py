from selene import browser, have
from module.pop_up import close_pop_up, close_pop_up_adv
from pages.main_page import MainPage
main_page = MainPage()

def test_authorization_successful(browser_management):
    main_page.open_main_page()
    main_page.open_authorization_page()
    main_page.fill_login()
    main_page.click_button_continue()
    main_page.fill_password()
    main_page.click_button_enter()
    main_page.close_number_pop_up()
    main_page.open_profile()
    main_page.should_authorization_success()


def test_authorization_failed(browser_management):
    main_page.open_main_page()
    main_page.open_authorization_page()
    main_page.fill_login()
    main_page.click_button_continue()
    main_page.fill_fake_password()
    main_page.click_button_enter()
    main_page.should_validation_massage()