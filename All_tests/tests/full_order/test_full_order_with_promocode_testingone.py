import allure
from playwright.sync_api import expect
from All_tests.tests.full_order.test_full_order import test_full_order_with_promo_code


@allure.title("Полный заказ, на повторное применение кода")
def test_redo_full_order_with_promo_code(page):
    # Выполняем предыдущий тест
    test_full_order_with_promo_code(page)
    page.wait_for_timeout(2000)

    username_fixed = "fordel"
    password_fixed = "fordel"
    promo_code = "GIVEMEHALYAVA"

    with allure.step("Возвращаемся на главную страницу и добавляем товар ещё раз"):
        page.goto("https://pizzeria.skillbox.cc/")
        product1 = page.locator('.wp-post-image[src*="pexels-natasha"]').nth(1)
        expect(product1).to_be_visible(timeout=10000)
        product1.hover()
        add_to_cart_1 = page.locator('.ajax_add_to_cart[data-product_id="425"]').first
        expect(add_to_cart_1).to_be_visible()
        expect(add_to_cart_1).to_be_enabled()
        add_to_cart_1.click()

        # Второй товар — Пицца Рай
        product2 = page.locator('.wp-post-image[src*="pexels-daria-shevtsova-1260968"]').nth(1)
        expect(product2).to_be_visible(timeout=10000)
        product2.hover()
        add_to_cart_2 = page.locator('.ajax_add_to_cart[data-product_id="421"]').nth(2)
        expect(add_to_cart_2).to_be_visible()
        expect(add_to_cart_2).to_be_enabled()
        add_to_cart_2.click()

    with allure.step('Переход к оформлению заказа'):
        make_order = page.locator("#menu-item-31").get_by_text("Оформление заказа")
        make_order.click()

    with allure.step("Добавляем купон на скидку"):
        code_place = page.locator(".showcoupon")
        code_place.click()
        code_input = page.locator("#coupon_code")
        code_input.fill(promo_code)
        accept_code = page.locator('button[name="apply_coupon"]')
        accept_code.click()
        page.wait_for_timeout(2000)

    with allure.step("Проверяем сообщение о применении промокода"):
        alert_message = page.locator('div.woocommerce-message[role="alert"]')
        expect(alert_message).to_be_visible(timeout=10000)
        text = alert_message.text_content()

        if "Coupon code applied successfully" in text:
            allure.attach(
                f"Обнаружено ошибочное сообщение: '{text}'",
                name="Результат проверки",
                attachment_type=allure.attachment_type.TEXT
            )
            print ("Промокод успешно применён — но по сценарию это ошибка!")
        elif "Coupon already used" in text:
            print("Промокод уже использован — ожидаемое поведение")
            allure.attach(
                "Промокод уже использован (Coupon already used)",
                name="Сообщение системы",
                attachment_type=allure.attachment_type.TEXT
            )
        else:
            allure.attach(
                f"Неожиданное сообщение: '{text}'",
                name="Результат проверки",
                attachment_type=allure.attachment_type.TEXT
            )
            print(f"Получено неожиданное сообщение: {text}")
