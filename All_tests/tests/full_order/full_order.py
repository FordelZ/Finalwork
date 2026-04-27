import allure
from playwright.sync_api import expect
from All_tests.tests.add_shopping_cart.fill_shopping_cart import fill_cart


@allure.title("Сценарий №1: Применение промокода GIVEMEHALYAVA (скидка 10%)")
def test_promo_code_discount_10percent(page):
    fill_cart(page)
    username_fixed = "fordel"
    password_fixed = "fordel"
    promo_code = "GIVEMEHALYAVA"
    order_name = "Vit"
    second_order_name = "Vit"
    address_test = "Ул. Пушкина д.123"
    city_test = "Test_city"
    area_test = "Test_area"
    postal_code_test = "100001"
    telephone_test = "89998007050"
    email_test = "Test@life.ru"

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

    with allure.step("Заполняем данные в деталях заказа"):
        order = page.locator('#billing_first_name')
        order.send_keys(order_name)
        second_order = page.locator('#billing_last_name')
        second_order.send_keys(second_order_name)
        address = page.locator('#billing_address_1')
        address.send_keys(address_test)
        city = page.locator('#billing_city')
        city.send_keys(city_test)
        area = page.locator('#billing_state')
        area.send_keys(area_test)
        postal = page.locator('#billing_postcode')
        postal.send_keys(postal_code_test)
        telephone = page.locator('#billing_phone')
        telephone.send_keys(telephone_test)
        email = page.locator('#billing_email')
        email.send_keys(email_test)
        checkbox = page.locator('#terms').click()
        checkbox.click()

    with allure.step("Выбираем страну 'Russia' в выпадающем списке"):
        country_dropdown = page.locator('.select2-selection.select2-selection--single')
        expect(country_dropdown).to_be_visible()
        country_dropdown.click()
        results_container = page.locator('#select2-billing_country-results')
        expect(results_container).to_be_visible(timeout=5000)
        page.wait_for_timeout(300)
        russia_option = page.locator('li.select2-results__option:has-text("Russia")')
        expect(russia_option).to_be_visible()
        russia_option.click()

    with allure.step("Завершаем оформление заказа и нажимаем кнопку 'Оформить заказ'"):
        accept_order = page.locator('[name="woocommerce_checkout_place_order"]')
        accept_order.click()