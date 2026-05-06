import allure

from playwright.sync_api import expect
from All_tests.tests.main_client_flow.test_4_menu_deserts import test_menu_with_deserts


@allure.title("Создание аккаунта")
def test_making_account(page):
    test_menu_with_deserts(page)

    test_username = "fordel4"
    test_password = "fordel"
    test_email = "fordel4@mail.ru"

    with allure.step('1. Переход в корзину заказа и нажимаем кнопку оформить заказ'):
        make_order = page.locator("#menu-item-29").get_by_text("Корзина")
        make_order.click()

        order_apply_button = page.locator('a:has-text("ПЕРЕЙТИ К ОПЛАТЕ")')
        order_apply_button.click()

        my_account_link = page.locator('#menu-item-30 a')
        my_account_link.click()

        register_button = page.locator('.custom-register-button')
        register_button.click()

    with allure.step("2. Проходим регистрацию"):
        username_input = page.locator('#reg_username')
        username_input.fill(test_username)

        email_input = page.locator('#reg_email')
        email_input.fill(test_email)

        password_input = page.locator('#reg_password')
        password_input.fill(test_password)

        apply_register_button = page.locator('button[name="register"]')
        apply_register_button.click()

    with allure.step("3. Переходим в мой аккаунт и проверяем авторизацию"):
        my_account_link = page.locator('#menu-item-30 a')
        my_account_link.click()

    welcome_username = page.locator('div.woocommerce-MyAccount-content p:has-text("Привет") strong')
    welcome_text = welcome_username.text_content()
    welcome_text_clean = welcome_text.strip()

    # Теперь шаги Allure содержат только синхронные операции
    with allure.step("1. Находим элемент приветствия"):
        # Просто отмечаем шаг — операция уже выполнена
        pass

    with allure.step("2. Получаем текст приветствия"):
        allure.attach(
            f"Ожидаемое имя: {test_username}\nФактическое имя: {welcome_text_clean}",
            name="Проверка приветствия",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("3. Проверяем совпадение имён"):
        assert welcome_text_clean == test_username, \
            f"Приветствие '{welcome_text_clean}' не совпадает с ожидаемым '{test_username}'"
