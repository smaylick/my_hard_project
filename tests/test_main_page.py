from selene import browser, have

from module.pop_up import close_pop_up


def test_catalog_display(browser_management):
    browser.open('/')  # захожу на сайт
    browser.element('[href*="login"]').click()  # кликаю на кнопку "Войти" в правой верхней части сайта
    browser.element('[name="email"]').type('taullessafunnoi-4696@yopmail.com')  # ввожу валидный логин
    browser.element('[type="submit"][class*="Button-module"]').click()  # кликаю на кнопку "Продолжить"
    browser.element('[name="pwd"]').type('verynicepassword')  # ввожу валидный пароль
    browser.element('.Button-module__button_2hpyT').click()  # кликаю на кнопку "Войти"
    close_pop_up()  # закрываю окно, которое всплывает
    browser.element('[class*="CatalogButton"]').should(have.exact_text('Каталог'))
