from selene import browser, have


class MainPage:
    def open_main_page(self):
        browser.open('/')
        return self

    def open_authorization_page(self):
        browser.element('[href*="login"]').click()
        return self

    def fill_login(self, login):
        browser.element('[name="email"]').type(login)
        return self

    def click_button_continue(self):
        browser.element('[type="submit"][class*="Button-module"]').click()
        return self

    def fill_password(self, password):
        browser.element('[name="pwd"]').type(password)
        return self

    def fill_fake_password(self, password):
        browser.element('[name="pwd"]').type(password)
        return self

    def click_button_enter(self):
        browser.element('.Button-module__button_2hpyT').click()
        return self

    def close_number_pop_up(self):
        browser.element('[class*="button_secondary"]').click()
        return self

    def open_profile(self):
        browser.element('[class*="logo_container"]').click()
        return self

    def should_authorization_success(self):
        browser.element('.Avatar-module__topContent_3OnBY').should(have.text('taullessafunnoi-4696'))
        return self

    def should_validation_massage(self):
        browser.element('[class*=input__error]').should(have.text('Неверное сочетание логина и пароля'))
        return self

    def should_have_catalog(self):
        browser.element('[class*="CatalogButton"]').should(have.exact_text('Каталог'))
        return self

    def authorization_success(self):
        browser.open('/')
        browser.element('[href*="login"]').click()
        browser.element('[name="email"]').type('taullessafunnoi-4696@yopmail.com')
        browser.element('[type="submit"][class*="Button-module"]').click()
        browser.element('[name="pwd"]').type('verynicepassword')
        browser.element('.Button-module__button_2hpyT').click()
        browser.element('[class*="button_secondary"]').click()
        return self


main_page = MainPage()
