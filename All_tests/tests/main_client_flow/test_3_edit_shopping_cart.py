import allure

from playwright.sync_api import expect

from All_tests.tests.main_client_flow.test_2_get_details_for_pizza import test_scroll_and_add_pizza


@allure.title("Редактирование корзины")
def test_edit_shopping_cart(page):
    test_scroll_and_add_pizza(page)

    with allure.step("1. Добавляем несколько пицц через клик"):
        adding_one = page.locator(
            'tr:has-text(\'Пицца "4 в 1"\'):has-text("Дополнительно: Сырный борт") .input-text.qty.text')
        adding_one.hover()
        adding_one.click()
        page.keyboard.press("ArrowUp")

    with allure.step("2. Обновление корзины"):
        update_button = page.locator('button[name="update_cart"]')
        update_button.click()

    with allure.step("3. Удаление пиццы из корзины"):
        product_row = page.locator(
            'tr:has(td.product-name:has-text("4 в 1")) '
            ':not(:has(td:has-text("Дополнительно: Сырный борт")))'
        )
        # Внутри строки ищем кнопку удаления
        delete_one = product_row.get_by_role('link', name='Remove this item').nth(1)
        delete_one.click()

        print("Ура?")
