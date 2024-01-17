from selene import browser, have


class FavoritePage:

    def find_item(self):
        browser.element('.SearchForm-module__input_2AIbu').type('слово пацана').press_enter()
        return self

    def open_page_item(self):
        browser.element('[href*="68307263"]').click()
        return self

    def click_add_to_favorites(self):
        browser.element('[class*="adaptive"] [class="FunctionalButton-module__funcButtonContent_-igzJ"]').click()
        return self

    def open_favorites(self):
        browser.element('[role="tab-favorite"]').click()
        return self

    def open_action_menu_item(self):
        browser.element('[class*="dropdown-dots"]').click()
        return self

    def clear_favorites(self):
        browser.element('[class*="art-buttons__drop"]').click()
        return self


favorite_page = FavoritePage()
