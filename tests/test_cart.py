from selene import browser

from module.pop_up import close_pop_up, close_pop_up_adv


def test_item_add_and_delete_cart(browser_management):
    browser.open('/')  # захожу на сайт
    browser.element('[href*="login"]').click()  # кликаю на кнопку "Войти" в правой верхней части сайта
    browser.element('[name="email"]').type('taullessafunnoi-4696@yopmail.com')  # ввожу валидный логин
    browser.element('[type="submit"][class*="Button-module"]').click()  # кликаю на кнопку "Продолжить"
    browser.element('[name="pwd"]').type('verynicepassword')  # ввожу валидный пароль
    browser.element('.Button-module__button_2hpyT').click()  # кликаю на кнопку "Войти"
    close_pop_up()  # закрываю окно, которое всплывает
    browser.element('.SearchForm-module__input_2AIbu').type('Антидемон. Книга 10').press_enter()  # ищу в поиске книгу
    browser.element('[href*="70190914"]').click()  # открываю страничку с книгой
    browser.element('[class*="391UX Button-module__button_s"]').click()  # кликаю на кнопку "Добавить в корзину"
    close_pop_up_adv()  # закрываю рекламное окно
    browser.element('[class="Tab-modules__tab__link_3MFWj"][href*="new_basket"]').click()  # открываю корзину
    browser.element('[data-test-id*="cart__listDeleteButton"]').click()  # удаляю товар из корзины
    browser.element(
        '[class*="Button-module__button_medium_2XZ9k Button-module__button_primary_2FaKg"]').click()  # подтверждаю удаление товара из корзины
