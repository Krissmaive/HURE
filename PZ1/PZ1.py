# Додаємо шлях до бібліотеки вручну (бо Python не бачить site-packages)
import sys

sys.path.append(r"E:\lib\site-packages")  # ← тут лежить requests та інші

# Імпорт потрібних модулів
import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime

# 1. Отримати курси євро за попередній тиждень, вивести дату + курс
url = "https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250317&end=20250321&valcode=eur&json"
response = requests.get(url)
data = json.loads(response.content)

# Підготовка списків для графіка
dates = []
rates = []

# Обхід даних
for item in data:
    date_str = item['exchangedate']  # формат "17.03.2025"
    rate = item['rate']

    print(f"{date_str} - {rate} грн")

    # Перетворення дати для графіка
    date_obj = datetime.strptime(date_str, "%d.%m.%Y")
    dates.append(date_obj)
    rates.append(rate)

# Matplotlib — побудова графіка
plt.plot(dates, rates, marker='o')
plt.title("Курс EUR до UAH за тиждень")
plt.xlabel("Дата")
plt.ylabel("Курс (грн)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
