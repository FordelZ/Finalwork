from playwright.sync_api import Playwright


config = {
    "test_dir": "All_tests.tests.add_shopping_cart",  # Точный путь к папке с тестами
    "use": {
        "headless": False,
        "slow_mo": 500,
        "screenshot": "only-on-failure",
        "video": "retain-on-failure"
    },
    "test_match": [
        "*test*.py",      # Шаблон: файлы с "test" в имени
        "*spec.py",     # Шаблон: файлы с "spec" в имени
        "*.py"          # Все Python‑файлы (если нужны все)
    ]
}

