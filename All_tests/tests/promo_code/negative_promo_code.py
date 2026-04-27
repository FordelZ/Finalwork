import allure
import re
from playwright.sync_api import expect

from All_tests.tests.add_shopping_cart.fill_shopping_cart import fill_cart


@allure.title("Сценарий №2: Проверка неприменения промокода DC120")
def test_promo_code_dc120_not_applied(page):
    fill_cart(page)
    username_fixed = "fordel"
    password_fixed = "fordel"
    promo_code = "DC120"

    with allure.step('Переход к оформлению заказа'):
        make_order = page.locator("#menu-item-31").get_by_text("Оформление заказа")
        make_order.click()

    with allure.step("Добавляем купон на скидку"):
        code_place = page.locator(".showcoupon")
        code_place.click()
        code_input = page.locator("#coupon_code")
        code_input.send_keys(promo_code)
        page.wait_for_timeout(2000)

    with allure.step("Находим конечную сумму заказа"):
        total_price = page.locator('bdi:has(span.woocommerce-Price-currencySymbol):nth-match(1)')
        expect(total_price).to_be_visible(timeout=10000)
        total_price_text = total_price.text_content().strip()
        cleaned_price = re.sub(r'[^\d.,]', '', total_price_text)
        normalized_price = cleaned_price.replace(',', '.')
        first_number = float(normalized_price)

        final_price = page.locator('bdi:has(span.woocommerce-Price-currencySymbol):nth-match(2)')
        expect(final_price).to_be_visible(timeout=10000)
        second_number_text = final_price.text_content().strip()
        cleaned_second = re.sub(r'[^\d.,]', '', second_number_text)
        normalized_second = cleaned_second.replace(',', '.')
        second_number = float(normalized_second)

        tolerance = 0.01

        print(f"Числа: {first_number} == {second_number}")

        allure.attach(
            f"{first_number} vs {second_number} (±{tolerance})",
            name="Сравнение чисел",
            attachment_type=allure.attachment_type.TEXT)
        assert abs(first_number - second_number) < tolerance, (
            f"Числа не равны: {first_number} ≠ {second_number}"
        )

    print("✓ Числа равны в пределах допустимой погрешности")
