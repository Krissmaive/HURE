# 3. Статистика продажів
sales = [
    {"продукт": "яблуко", "кількість": 10, "ціна": 5},
    {"продукт": "банан", "кількість": 20, "ціна": 2},
    {"продукт": "молоко", "кількість": 50, "ціна": 25},
    {"продукт": "молоко", "кількість": 10, "ціна": 25},
]

def total_income(sales):
    income = {}
    for sale in sales:
        product = sale["продукт"]
        revenue = sale["кількість"] * sale["ціна"]
        income[product] = income.get(product, 0) + revenue
    high_earners = [product for product, total in income.items() if total > 1000]
    return income, high_earners

def demo_sales():
    income, big_income = total_income(sales)
    print("Загальний дохід:", income)
    print("Продукти з доходом > 1000:", big_income)

if __name__ == "__main__":
    demo_sales()
