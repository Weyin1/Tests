import os
import sys
import requests

TOKEN = os.environ.get("BOT_TOKEN")
APP_URL = os.environ.get("APP_URL")

if not TOKEN or not APP_URL:
    print('Нужно указать BOT_TOKEN и APP_URL, например:')
    print('BOT_TOKEN="123:ABC" APP_URL="https://example.com/index.html" python set_menu_button.py')
    sys.exit(1)

response = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/setChatMenuButton",
    json={
        "menu_button": {
            "type": "web_app",
            "text": "Тренажёр",
            "web_app": {"url": APP_URL},
        }
    },
    timeout=20,
)

print(response.status_code)
print(response.text)
response.raise_for_status()
print("Готово: кнопка меню бота привязана к Mini App.")
