# 2. Інвентаризація продуктів
inventory = {
    "яблуко": 10,
    "банан": 2,
    "молоко": 3
}

def update_inventory(product, quantity):
    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity

def low_stock():
    return [product for product, qty in inventory.items() if qty < 5]

def demo_inventory():
    update_inventory("яблуко", -5)
    print("Оновлений склад:", inventory)
    print("Мало на складі:", low_stock())

if __name__ == "__main__":
    demo_inventory()
