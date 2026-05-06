import allure

from playwright.sync_api import expect


@allure.title("Авторизация пользователя")
def tests_registration(page):
    account_username = "Fordel"
    account_password = ""

    with allure.step('1. Переход на страницу сайта авторизации'):
        page.goto("https://pizzeria.skillbox.cc/my-account/")

    with allure.step("2. Вводим email и пароль верно, поле имя оставляем пустым"):
        username_input = page.locator('#username')
        username_input.fill(account_username)

        password_input = page.locator('#password')
        password_input.fill(account_password)

    with allure.step("3. Нажимаем кнопку подтвердить авторизацию"):
        apply_register_button = page.locator('button[name="login"]')
        apply_register_button.click()

    with allure.step("4. Проверяем что выдало ошибку в поле Пароль"):
        error_message = page.get_by_role('alert')
        expect(error_message).to_be_visible(timeout=10000)
        print("Ошибка ввода Пароль обнаружена")

        error_text = error_message.text_content()
        error_message_text = error_text.strip()

        allure.attach(
            "Ошибка ввода Пароль обнаружена\n"
            "Необходимо заполнить поле - Пароль "
        )
        print(error_message_text)
