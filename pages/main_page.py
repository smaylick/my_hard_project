from selene import browser, have


class MainPage:
    def open_main_page(self):
        browser.open('/')
        return self

    def open_authorization_page(self):
        browser.element('[href*="login"]').click()
        return self

    def fill_login(self):
        browser.element('[name="email"]').type('taullessafunnoi-4696@yopmail.com')
        return self

    def click_button_continue(self):
        browser.element('[type="submit"][class*="Button-module"]').click()
        return self

    def fill_password(self):
        browser.element('[name="pwd"]').type('verynicepassword')
        return self

    def fill_fake_password(self):
        browser.element('[name="pwd"]').type('fakepassword')
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
