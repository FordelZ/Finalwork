import allure

from playwright.sync_api import expect


@allure.title("Регистрация нового пользователя")
def tests_registration(page):
    account_username = "fordelZ"
    account_password = "1234"
    account_email = "fordelmail.ru"


    with allure.step('1. Переход на страницу сайта регистрации'):
        page.goto("https://pizzeria.skillbox.cc/register/")

    with allure.step("2. Вводим email и пароль верно, поле имя оставляем пустым"):
        username_input = page.locator('#reg_username')
        username_input.fill(account_username)

        email_input = page.locator('#reg_email')
        email_input.fill(account_email)

        password_input = page.locator('#reg_password')
        password_input.fill(account_password)

        apply_register_button = page.locator('button[name="register"]')
        apply_register_button.click()

    with allure.step("3. Нажимаем кнопку подтвердить регистрацию"):
        apply_register_button = page.locator('button[name="register"]')
        apply_register_button.click()

    with allure.step("4. Проверяем что выдало ошибку в поле Email"):
        error_message = page.get_by_role('alert')
        expect(error_message).to_be_visible(timeout=10000)
        print("Ошибка ввода email обнаружена")

        error_text = error_message.text_content()
        error_message_text = error_text.strip()

        allure.attach(
            f"Ошибка ввода Email обнаружена\n"
            f"Необходимо заполнить поле - Email "
        )
        print(error_message_text)