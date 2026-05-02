import allure

from playwright.sync_api import expect
from All_tests.tests.add_shopping_cart.test_fill_shopping_cart import test_fill_cart


@allure.title("Сценарий №3: Применение промокода GIVEMEHALYAVA, перехват запроса")
def test_promo_code_error_500(page):
    test_fill_cart(page)
    username_fixed = "fordel"
    password_fixed = "fordel"
    promo_code = "GIVEMEHALYAVA"

    with allure.step('Переход к оформлению заказа'):
        make_order = page.locator("#menu-item-31").get_by_text("Оформление заказа")
        make_order.click()

        code_place = page.locator(".showcoupon")
        code_place.click()

    with allure.step("Перехват запроса"):
        page.route("**/?wc-ajax=apply_coupon", lambda route: route.fulfill(
            status=500,
            body="Internal Server Error"
        ))

    with allure.step("Добавляем купон на скидку"):

        code_input = page.locator("#coupon_code")
        code_input.fill(promo_code)

        accept_code = page.locator('button[name="apply_coupon"]')
        accept_code.click()
        page.wait_for_timeout(2000)

    with allure.step("Авторизуемся с данными пользователя"):
        authorization = page.locator('a.showlogin[href="#"]')
        authorization.click()

        username = page.locator("#username")
        username.fill(username_fixed)

        password = page.locator("#password")
        password.fill(password_fixed)

        enter_profile = page.locator('button[name="login"]')
        enter_profile.click()

    with allure.step("Находим цену после скидки"):
        discount_locator = page.locator('bdi:has(span.woocommerce-Price-currencySymbol):nth-match(2)')
        expect(discount_locator).to_be_visible(timeout=10000)
        total_price_text = discount_locator.text_content().strip()
        cleaned = re.sub(r'[^\d.,]', '', total_price_text)
        normalized = cleaned.replace(',', '.')
        total_price = float(normalized)
        ten_percent = total_price * 0.1
        ten_percent_rounded = round(ten_percent, 2)

    with allure.step("Находим конечную сумму заказа"):
        price_locator = page.locator('bdi:has(span.woocommerce-Price-currencySymbol):nth-match(1)')
        expect(price_locator).to_be_visible(timeout=10000)
        discount_text = price_locator.text_content().strip()
        cleaned_discount = re.sub(r'[^\d.,]', '', discount_text)
        normalized_discount = cleaned_discount.replace(',', '.')
        discount_value = float(normalized_discount)

    with allure.step("Сравниваем вычисленные 10% с третьим числом"):
        assert abs(ten_percent_rounded - discount_value) < 0.01, (
            f"Вычисленные 10% ({ten_percent_rounded}) не равны третьему числу на странице ({discount_value}). "
            f"Разница: {abs(ten_percent_rounded - discount_value)}"
        )

        allure.attach(
            f"Итоговая сумма: {total_price}\n"
            f"10% от суммы: {ten_percent_rounded}\n"
            f"Третье число на странице: {discount_value}\n"
            f"Результат сравнения: {'✓ Успешно' if abs(ten_percent_rounded - discount_value) < 0.01 else '✗ Ошибка'}",
            name="Результаты сравнения",
            attachment_type=allure.attachment_type.TEXT
        )

        print(f" Вычисленные 10%: {ten_percent_rounded}")
        print(f" Третье число: {discount_value}")