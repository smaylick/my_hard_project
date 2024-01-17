import allure
from pages.cart_page import cart_page
from pages.main_page import main_page


class TestCart:

    @allure.title("Adding and removing a book to cart")
    def test_item_add_and_delete_cart(self, browser_management):
        with allure.step("Successful authorization"):
            main_page.authorization_success()
        with allure.step("Book search"):
            cart_page.find_item()
        with allure.step("Open product page"):
            cart_page.open_page_item()
        with allure.step("Click add to cart"):
            cart_page.click_add_to_cart()
        with allure.step("Open cart"):
            cart_page.open_cart()
        with allure.step("Clear cart"):
            cart_page.clear_cart()
        with allure.step("Confirm clear cart"):
            cart_page.confirm_clear_cart()