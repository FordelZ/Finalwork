import re
import allure
from playwright.sync_api import expect
from All_tests.tests.add_shopping_cart.fill_shopping_cart import fill_cart


@allure.title("Сценарий №1: Применение промокода GIVEMEHALYAVA (скидка 10%)")
def test_promo_code_discount_10percent(page):
    fill_cart(page)
    username_fixed = "fordel"
    password_fixed = "fordel"
    promo_code = "GIVEMEHALYAVA"
    discount_percent = 10

    with allure.step('Переход к оформлению заказа'):
        make_order = page.locator("#menu-item-31").get_by_text("Оформление заказа")
        make_order.click()

    with allure.step('Переходим в окно авторизации'):
        authorization = page.locator('a.showlogin[href="#"]')
        #authorization = page.locator('xpath=//a[@class="showlogin" and text()="Авторизуйтесь"]')
        #authorization = page.get_by_role('link', name='Авторизуйтесь', exact=True)
        #authorization = page.locator('.showlogin')
        authorization.click()

    with allure.step("Авторизуемся с данными пользователя"):
        username = page.locator("#username")
        username.send_keys(username_fixed)
        password = page.locator("#password")
        password.send_keys(password_fixed)

    with allure.step("Добавляем купон на скидку"):
        code_place = page.locator(".showcoupon")
        code_place.click()
        code_input = page.locator("#coupon_code")
        code_input.send_keys(promo_code)
        page.wait_for_timeout(2000)

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
        print(" Значения совпадают в пределах допустимой погрешности")

