import allure


@allure.title("Сценарий №1: Применение промокода GIVEMEHALYAVA (скидка 10%)")
def fill_cart(page):

    with allure.step("1. Заполняем корзину любыми товарами"):
        # 1) Переход на главную страницу
        page.goto("https://pizzeria.skillbox.cc/")

        # 2) Добавление товара в корзину
        page.wait_for_selector('//*[@id="accesspress_store_product-5"]/ul/div/div/li[5]/div/a[2]')
        page.click('//*[@id="accesspress_store_product-5"]')

        page.wait_for_selector('//*[@id="accesspress_store_product-5"]/ul/div/div/li[6]/div/a[2]')
        page.click('//*[@id="accesspress_store_product-5"]/ul/div/div/li[6]/div/a[2]')

