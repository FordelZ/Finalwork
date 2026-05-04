import asyncio
import allure
from playwright.async_api import expect

@allure.title("Заполнение корзины")
async def test_shit(page):
    with allure.step("1. Переходим на главную страницу"):
        await page.goto("https://pizzeria.skillbox.cc/", wait_until="load")

    with allure.step("2. Добавляем первый товар в корзину"):
        # Первый товар - Пицца 4 В 1
        product1 = page.locator('.wp-post-image[src*="pexels-natasha"]').nth(1)
        await expect(product1).to_be_visible(timeout=10000)
        await product1.hover()
        add_to_cart_1 = page.locator('.ajax_add_to_cart[data-product_id="425"]').first
        await expect(add_to_cart_1).to_be_visible()
        await expect(add_to_cart_1).to_be_enabled()
        await add_to_cart_1.click()

    with allure.step("3. Находим кнопку слайдера и кликаем Next 3 раза"):
        slider = page.locator('.item-img a[href*="/product/"]')
        await slider.hover()

        next_button = page.locator('a.slick-next')
        for i in range(3):
            await next_button.wait_for(state='visible', timeout=5000)
            if await next_button.is_enabled():
                await next_button.click()
                print(f"Клик {i + 1} выполнен")
                await page.wait_for_timeout(300)  # Небольшая пауза между кликами
            else:
                print("Кнопка Next неактивна, прерываем цикл")
                break
