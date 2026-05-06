import allure
from playwright.sync_api import expect


@allure.title("Заполнение корзины")
def test_fill_cart(page):
    with allure.step("1. Переходим на главную страницу"):
        page.goto("https://pizzeria.skillbox.cc/", wait_until="load")

    with allure.step("2. Добавляем первый товар в корзину"):

        # Первый товар - Пицца 4 В 1
        product1 = page.locator('.wp-post-image[src*="pexels-natasha"]').nth(1)
        expect(product1).to_be_visible(timeout=10000)
        product1.hover()
        add_to_cart_1 = page.locator('.ajax_add_to_cart[data-product_id="425"]').first
        expect(add_to_cart_1).to_be_visible()
        expect(add_to_cart_1).to_be_enabled()
        add_to_cart_1.click()

        # Второй товар - Пицца Рай
        product2 = page.locator('.wp-post-image[src*="pexels-daria-shevtsova-1260968"]').nth(1)
        expect(product2).to_be_visible(timeout=10000)
        product2.hover()
        add_to_cart_2 = page.locator('.ajax_add_to_cart[data-product_id="421"]').nth(2)
        expect(add_to_cart_2).to_be_visible()
        expect(add_to_cart_2).to_be_enabled()
        add_to_cart_2.click()

        # Третий товар - Пицца Как у Бабушки
        product3 = page.locator('.wp-post-image[src*="pexels-katerina-holmes-5908222"]').nth(1)
        expect(product3).to_be_visible(timeout=10000)
        product3.hover()
        add_to_cart_3 = page.locator('.ajax_add_to_cart[data-product_id="423"]').nth(2)
        expect(add_to_cart_3).to_be_visible()
        expect(add_to_cart_3).to_be_enabled()
        add_to_cart_3.click()

    with allure.step("3 Проверяем добавленные товары"):
        checking_order = page.locator('.cart-contents.wcmenucart-contents')
        checking_order.click()

    rows = page.locator('tr.woocommerce-cart-form__cart-item.cart_item').all()
    for i, row in enumerate(rows):
        name = row.locator('td.product-name a').text_content()
        price = row.locator('td.product-price .woocommerce-Price-amount').text_content()
        print(f"Товар {i + 1}: {name} — {price}")
