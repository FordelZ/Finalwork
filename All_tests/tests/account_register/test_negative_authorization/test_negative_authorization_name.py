import allure

from playwright.sync_api import expect


@allure.title("Авторизация пользователя")
def tests_registration(page):
    account_username = ""
    account_password = "fordel"


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

    with allure.step("4. Проверяем что выдало ошибку в поле Имя"):
        error_message = page.get_by_role('alert')
        expect(error_message).to_be_visible(timeout=10000)
        print("Ошибка ввода имени обнаружена")

        error_text = error_message.text_content()
        error_message_text = error_text.strip()

        allure.attach(
            f"Ошибка ввода Имя обнаружена\n"
            f"Необходимо заполнить поле - Имя "
        )
        print(error_message_text)