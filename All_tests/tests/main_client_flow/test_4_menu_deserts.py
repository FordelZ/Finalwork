import allure

from playwright.sync_api import expect

from All_tests.tests.main_client_flow.test_3_edit_shopping_cart import test_edit_shopping_cart


@allure.title("Редактирование корзины")
def test_menu_with_deserts(page):
    test_edit_shopping_cart(page)

    with allure.step("1. Переходим в десерты"):
        page.locator('#menu-item-389 > a:has-text("Меню")').click()
        deserts_button = page.locator('#menu-item-391 a')
        deserts_button.click()

    with allure.step("2. Настроить фильтр"):
        right_handle = page.locator('.price_slider span.ui-slider-handle').nth(1)
        right_handle.drag_to(
            page.locator('.price_slider'),
            target_position={'x': 90, 'y': 0}  # перемещаю по x
        )

    with allure.step("3. Применить фильтр цены"):
        apply_button = page.get_by_role('button', name='Применить')
        apply_button.click()

    with allure.step("4. Добавляем десерт"):
        add_to_cart = page.locator('a[data-product_id="437"]')
        add_to_cart.click()

    print("Yalla")
