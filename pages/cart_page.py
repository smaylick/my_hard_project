from selene import browser


class CartPage:

    def find_item(self):
        browser.element('.SearchForm-module__input_2AIbu').type('Антидемон. Книга 10').press_enter()
        return self

    def open_page_item(self):
        browser.element('[href*="70190914"]').click()
        return self

    def click_add_to_cart(self):
        browser.element('[class*="391UX Button-module__button_s"]').click()
        return self

    def close_pop_up_adv(self):
        browser.element('[class*="close_r"]').click()
        return self

    def open_cart(self):
        browser.element('[class="Tab-modules__tab__link_3MFWj"][href*="new_basket"]').click()
        return self

    def clear_cart(self):
        browser.element('[data-test-id*="cart__listDeleteButton"]').click()
        return self

    def confirm_clear_cart(self):
        browser.element('[class*="Button-module__button_medium_2XZ9k Button-module__button_primary_2FaKg"]').click()
        return self


cart_page = CartPage()
