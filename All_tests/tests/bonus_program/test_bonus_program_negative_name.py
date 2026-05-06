import allure
from playwright.sync_api import expect


@allure.title("Флоу на бонусную программу: ")
def test_bonus_actions_negative(page):
    test_name = ""
    test_phone = "89008007060"

    with allure.step("1. Переходим на страницу сайта "):
        page.goto("https://pizzeria.skillbox.cc/", wait_until="load")
        bonus = page.locator('#menu-item-363 a')
        expect(bonus).to_be_visible(timeout=10000)
        bonus.click()

    with allure.step("2. Заполняем данные"):
        name_field = page.locator('#bonus_username')
        expect(name_field).to_be_visible(timeout=10000)
        name_field.fill(test_name)

        phone_field = page.locator('#bonus_phone')
        expect(phone_field).to_be_visible(timeout=10000)
        phone_field.fill(test_phone)

    with allure.step("3. Нажимаем на кнопку оформить карту"):
        accept_bonus = page.get_by_text('Оформить карту')
        expect(accept_bonus).to_be_visible(timeout=10000)
        accept_bonus.click()
        page.wait_for_timeout(2000)

    with allure.step("4. Проверяем что выдало ошибку в поле Имя"):
        error_message = page.locator('#bonus_content')
        expect(error_message).to_be_visible(timeout=10000)
        print("Ошибка ввода имени обнаружена")

        error_text = error_message.text_content()
        error_message_text = error_text.strip()

        allure.attach(
            "Ошибка ввода Имя обнаружена\n"
            "Необходимо заполнить поле - Имя "
        )
        print(error_message_text)
