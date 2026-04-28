#with allure.step("2. Добавляем первый товар в корзину"):
#    product = page.locator('.wp-post-image[src*="pexels-natasha"]').nth(1)
#    expect(product).to_be_visible(timeout=10000)
#   product.hover()
#    add_to_cart_2 = page.locator('.ajax_add_to_cart[data-product_id="425"]').first
#    expect(add_to_cart_2).to_be_visible()
#    expect(add_to_cart_2).to_be_enabled()
#    add_to_cart_2.click()
#
#    # with allure.step("2. Добавляем первый товар в корзину"):
#    product = page.locator('.wp-post-image[src*="pexels-natasha"]').nth(1)
#    expect(product).to_be_visible(timeout=10000)
#    product.hover()
#    add_to_cart_1 = page.locator('.ajax_add_to_cart[data-product_id="423"]').first
#    try:
#        expect(add_to_cart_1).to_be_attached(timeout=10000)
#        expect(add_to_cart_1).to_be_visible(timeout=5000)
#        expect(add_to_cart_1).to_be_enabled()
#    except Exception as e:
#        allure.attach(
#            f"Первая попытка не удалась: {e}",
#            name="Ошибка поиска кнопки",
#            attachment_type=allure.attachment_type.TEXT
#        )
#        # Повторная попытка найти кнопку
#        add_to_cart_1 = page.locator('.ajax_add_to_cart[data-product_id="423"]').first
#        expect(add_to_cart_1).to_be_attached(timeout=10000)
#        expect(add_to_cart_1).to_be_visible(timeout=5000)
#        expect(add_to_cart_1).to_be_enabled()
#
#    add_to_cart_1.scroll_into_view_if_needed()
#    add_to_cart_1.click(timeout=10000)

    # with allure.step("3. Добавляем второй товар в корзину"):
    # Альтернативный вариант: поиск по data‑атрибуту (если известен ID товара)
 #   add_to_cart_2 = page.locator('.ajax_add_to_cart[data-product_id="425"]').first
  #  expect(add_to_cart_2).to_be_visible()
   # expect(add_to_cart_2).to_be_enabled()
    #add_to_cart_2.click()

    # with allure.step("4. Проверяем, что товары добавлены в корзину"):
    # Ждём появления индикатора количества товаров в корзине
   # cart_badge = page.locator('.cart-contents')  # или другой селектор для иконки корзины
   # expect(cart_badge).to_be_visible(timeout=10000)
    # Проверяем, что количество товаров ≥ 2
  #  expect(cart_badge).to_have_text(r'\d+', timeout=10000)  # регулярное выражение для цифры
#
#print("✓ Корзина заполнена товарами")