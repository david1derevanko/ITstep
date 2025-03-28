class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock  # Кількість товару в наявності

    def is_available(self, quantity):
        return self.stock >= quantity

    def update_stock(self, quantity):
        if self.is_available(quantity):
            self.stock -= quantity
            return True
        return False

    def __str__(self):
        return f"{self.name}: {self.price} грн, В наявності: {self.stock} шт."

class Cart:
    def __init__(self):
        self.items = {}  # Словник {продукт: кількість}

    def add_product(self, product, quantity):
        if product.is_available(quantity):
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            product.update_stock(quantity)
            print(f"Додано {quantity} шт. {product.name} до кошика.")
        else:
            print(f"Недостатньо товару {product.name} на складі!")

    def remove_product(self, product, quantity):
        if product in self.items:
            if self.items[product] <= quantity:
                del self.items[product]
            else:
                self.items[product] -= quantity
            product.stock += quantity  # Повертаємо товар на склад
            print(f"Видалено {quantity} шт. {product.name} з кошика.")
        else:
            print(f"{product.name} відсутній у кошику.")

    def total_price(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def show_cart(self):
        if not self.items:
            print("Кошик порожній!")
        else:
            print("Кошик покупця:")
            for product, quantity in self.items.items():
                print(f"{product.name} - {quantity} шт.")


p1 = Product("Ноутбук", 25000, 5)
p2 = Product("Смартфон", 15000, 10)
p3 = Product("Навушники", 3000, 15)


cart = Cart()


cart.add_product(p1, 2)
cart.add_product(p2, 1)
cart.add_product(p3, 3)
cart.show_cart()
print(f"Загальна сума: {cart.total_price()} грн")

cart.remove_product(p3, 1)
cart.show_cart()
print(f"Загальна сума: {cart.total_price()} грн")