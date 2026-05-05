import allure
from playwright.sync_api import expect


@allure.title("Флоу на бонусную программу: ")
def test_bonus_actions(page):
    test_name = "Sick1"
    test_phone = "89008007060"


    with allure.step("1. Переходим на страницу сайта "):
        page.goto("https://pizzeria.skillbox.cc/", wait_until="load")
        bonus = page.locator('#menu-item-363 a')
        expect(bonus).to_be_visible(timeout=10000)
        bonus.click()

    with allure.step("Заполняем данные"):
        name_field = page.locator('#bonus_username')
        expect(name_field).to_be_visible(timeout=10000)
        name_field.fill(test_name)

        phone_field = page.locator('#bonus_phone')
        expect(phone_field).to_be_visible(timeout=10000)
        phone_field.fill(test_phone)

    with allure.step("Нажимаем на кнопку оформить карту"):
        accept_bonus = page.get_by_text('Оформить карту')
        expect(accept_bonus).to_be_visible(timeout=10000)
        accept_bonus.click()
        page.wait_for_timeout(2000)

    with allure.step("Проверяем отображение сообщения об успешной оформлении карты"):
        container = page.locator('#bonus_main h3')
        expect(container).to_be_visible(timeout=200000)
        expect(container).to_have_text(
            "Ваша карта оформлена!\n")

        allure.attach(
            "Блок с сообщением об оформлении карты найден и проверен",
            name="Результат проверки сообщения",
            attachment_type=allure.attachment_type.TEXT
        )

    print("Сообщение 'Ваша карта оформлена!' отображено")



    #бесконечная загрузка результатов ответа