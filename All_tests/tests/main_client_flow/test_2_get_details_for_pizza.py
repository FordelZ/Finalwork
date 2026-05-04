import allure

from playwright.sync_api import expect

from All_tests.tests.add_shopping_cart.test_fill_shopping_cart import test_fill_cart


@allure.title("Заполнение корзины")
def test_scroll_and_add_pizza(page):
    test_fill_cart(page)
    with allure.step("1. Переходим на главную страницу"):
        page.goto("https://pizzeria.skillbox.cc/", wait_until="load")

    with allure.step("2. Делаем скролл по меня и кликаем по пицце Пеперони" ):

        product1 = page.locator('.wp-post-image[src*="pexels-natasha"]').nth(1)
        expect(product1).to_be_visible(timeout=10000)
        product1.click()

    with allure.step("3. Выбираем виды пиццы и ставим Сырную"):
        select_locator = page.locator(".select")
        select_locator.click()
        select_locator.select_option('55.00')
        page.mouse.click(0, 0)
        page.wait_for_timeout(2000)

    with allure.step("4. Добавляем пиццу с выбранным наполнением"):
        finishing_order = page.locator('.single_add_to_cart_button')
        finishing_order.click()

    with allure.step('5. Переход к оформлению заказа'):
        make_order = page.locator("#menu-item-29").get_by_text("Корзина")
        make_order.click()

    with allure.step("6. Проверяем что заказ успешно добавлен"):
        page.wait_for_timeout(2000)
        correct_order = page.locator('dd.variation- p:has-text("Сырный борт")')
        extracted_text = correct_order.text_content()
        # Переменная для сравнения
        expected_text = "Сырный борт"
        # Сравниваем
        assert extracted_text == expected_text, f"Ожидался '{expected_text}', но найден '{extracted_text}'"
        print(extracted_text)
        print(expected_text)
