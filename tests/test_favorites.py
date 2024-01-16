from selene import browser

from module.pop_up import close_pop_up


def test_item_add_and_delete_favorites(browser_management):
    browser.open('/')  # захожу на сайт
    browser.element('[href*="login"]').click()  # кликаю на кнопку "Войти" в правой верхней части сайта
    browser.element('[name="email"]').type('taullessafunnoi-4696@yopmail.com')  # ввожу валидный логин
    browser.element('[type="submit"][class*="Button-module"]').click()  # кликаю на кнопку "Продолжить"
    browser.element('[name="pwd"]').type('verynicepassword')  # ввожу валидный пароль
    browser.element('.Button-module__button_2hpyT').click()  # кликаю на кнопку "Войти"
    close_pop_up()  # закрываю окно, которое всплывает
    browser.element('.SearchForm-module__input_2AIbu').type('слово пацана').press_enter()  # ищу в поиске книгу
    browser.element('[href*="68307263"]').click()  # открываю страничку с книгой
    browser.element(
        '[class*="adaptive"] [class="FunctionalButton-module__funcButtonContent_-igzJ"]').click()  # добавляю книгу в "Избранное"
    browser.element('[role="tab-favorite"]').click()  # кликаю на кнопку Избранное
    browser.element('[class*="dropdown-dots"]').click()  # открываю экшн-меню сущности
    browser.element('[class*="art-buttons__drop"]').click()  # удаляю товар из отложенного
