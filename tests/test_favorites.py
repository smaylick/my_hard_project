import allure
from pages.favorite_page import favorite_page
from pages.main_page import main_page


class TestFavorites:
    @allure.title("Adding and removing a book to favorites")
    def test_item_add_and_delete_favorites(self, browser_management):
        with allure.step("Successful authorization"):
            main_page.authorization_success()
        with allure.step("Book search"):
            favorite_page.find_item()
        with allure.step("Open product page"):
            favorite_page.open_page_item()
        with allure.step("Click add to favorites"):
            favorite_page.click_add_to_favorites()
        with allure.step("Open favorites"):
            favorite_page.open_favorites()
        with allure.step("Open item action menu"):
            favorite_page.open_action_menu_item()
        with allure.step("Clear favorites"):
            favorite_page.clear_favorites()