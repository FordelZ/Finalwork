import allure
import re
from playwright.sync_api import expect
from All_tests.tests.add_shopping_cart.test_fill_shopping_cart import test_fill_cart


@allure.title("Сценарий №2: Проверка неприменения промокода DC120")
def test_promo_code_dc120_not_applied(page):
    test_fill_cart(page)
    username_fixed = "fordel"
    password_fixed = "fordel"
    promo_code = "DC120"

    with allure.step('Переход к оформлению заказа'):
        make_order = page.locator("#menu-item-31").get_by_text("Оформление заказа")
        make_order.click()

    with allure.step("Авторизуемся с данными пользователя"):
        authorization = page.locator('a.showlogin[href="#"]')
        authorization.click()

        username = page.locator("#username")
        username.fill(username_fixed)

        password = page.locator("#password")
        password.fill(password_fixed)

        enter_profile = page.locator('button[name="login"]')
        enter_profile.click()

    with allure.step("Добавляем купон на скидку"):
        code_place = page.locator(".showcoupon")
        code_place.click()

        code_input = page.locator("#coupon_code")
        code_input.fill(promo_code)

        accept_code = page.locator('button[name="apply_coupon"]')
        accept_code.click()

    with allure.step("Проверяем что выдало ошибку при вводе промокода"):
        error_message = page.get_by_role('alert')
        expect(error_message).to_be_visible(timeout=10000)
        print("Ошибка ввода кода обнаружена")

        allure.attach(
            f"Ошибка при вводе кода обнаружена\n"
            f"Код не применился"
        )