import allure

from playwright.sync_api import expect
from All_tests.tests.main_client_flow.test_5_making_account import test_making_account


@allure.title("Редактирование корзины")
def test_finishing_client_flow(page):
    test_making_account(page)

    order_name = "Vit"
    second_order_name = "Vit"
    address_test = "Ул. Пушкина д.123"
    city_test = "Test_city"
    area_test = "Test_area"
    postal_code_test = "100001"
    telephone_test = "89998007050"
    email_test = "Test@life.ru"

    with allure.step('1. Переход в корзину заказа и нажимаем кнопку оформить заказ'):
        make_order = page.locator("#menu-item-29").get_by_text("Корзина")
        make_order.click()

        order_apply_button = page.locator('a:has-text("ПЕРЕЙТИ К ОПЛАТЕ")')
        order_apply_button.click()

    with allure.step("2. Заполняем данные в деталях заказа"):
        order = page.locator('#billing_first_name')
        order.fill(order_name)

        second_order = page.locator('#billing_last_name')
        second_order.fill(second_order_name)

        address = page.locator('#billing_address_1')
        address.fill(address_test)

        city = page.locator('#billing_city')
        city.fill(city_test)

        area = page.locator('#billing_state')
        area.fill(area_test)

        postal = page.locator('#billing_postcode')
        postal.fill(postal_code_test)

        telephone = page.locator('#billing_phone')
        telephone.fill(telephone_test)

        email = page.locator('#billing_email')
        email.fill(email_test)

        checkbox = page.locator('#terms')
        checkbox.click()

    with allure.step("3. Выбираем страну 'Russia' в выпадающем списке"):
        country_dropdown = page.locator('.select2-selection.select2-selection--single')
        expect(country_dropdown).to_be_visible()
        country_dropdown.click()
        results_container = page.locator('#select2-billing_country-results')
        expect(results_container).to_be_visible(timeout=5000)
        page.wait_for_timeout(300)
        russia_option = page.locator('li.select2-results__option:has-text("Russia")')
        expect(russia_option).to_be_visible()
        russia_option.click()

    with allure.step("4. Выбираем дату заказа"):
        order_date_input = page.locator('#order_date')
        order_date_input.fill('2026-05-05')

    with allure.step("5. Завершаем оформление заказа и нажимаем кнопку 'Оформить заказ'"):
        accept_order = page.locator('[name="woocommerce_checkout_place_order"]')
        accept_order.click()