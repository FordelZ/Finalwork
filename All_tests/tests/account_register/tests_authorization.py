import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestsPizzeria:
    @allure.title("Регистрация нового пользователя")
    def tests_authorization(self, selenium):
        account_username = "Fordel"

        with allure.step('Переход на страницу сайта'):
            selenium.get("http://pizzeria.skillbox.cc/")

        wait = WebDriverWait(selenium, 10)

        with allure.step('Открытие формы авторизации'):
            authorization_input = wait.until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/header/div[2]/div/div[2]/div[2]/a"))
            )
            authorization_input.click()

        with allure.step('Вводим в поле имя - Fordel'):
            username_input = wait.until(lambda d: d.find_element(By.NAME, 'username'))
            username_input.send_keys(account_username)

        with allure.step('Вводит пароль'):
            password_input = wait.until(lambda d: d.find_element(By.NAME, 'password'))
            password_input.send_keys("fordel")

        with allure.step('Нажимает кнопку Войти'):
            authorization_button = wait.until(
                lambda d: d.find_element(
                    (By.XPATH,
                     "/html/body/div[1]/div/div[2]/main/div/article/div/div/div/div/form/p[3]/button")
                )
            )
            authorization_button.click()
