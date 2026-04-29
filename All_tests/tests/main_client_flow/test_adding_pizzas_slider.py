import allure
import asyncio
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

    with allure.step("3.Находим кнопку слайдера"):
        async def click_next_three_times():
            slider = page.locator('.item-img a[href*="/product/"]')
            await slider.hover()

            next_button = page.locator('a.slick-next')
            for _ in range(3):
                await next_button.click()
                await click_next_three_times()
                print("Кликаю жестко")
