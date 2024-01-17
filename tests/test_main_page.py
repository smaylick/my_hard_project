import allure
from pages.main_page import main_page


class TestCatalog:
    @allure.title("Checking for directory availability")
    def test_catalog_display(self, browser_management):
        with allure.step("Successful authorization"):
            main_page.authorization_success()
        with allure.step("Checking for directory availability"):
            main_page.should_have_catalog()