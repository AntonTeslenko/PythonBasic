class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname} {self.numberphone}"


class Purchase:
    def __init__(self, user):
        self.user = user
        self.products = {}  # Словник для зберігання товарів і їхньої кількості

    def add_item(self, item, cnt):
        """
        Додає товар до замовлення. Якщо товар вже є, оновлюється кількість.
        """
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt

    def get_total(self):
        """
        Обчислює загальну вартість замовлення.
        """
        return sum(item.price * cnt for item, cnt in self.products.items())

    def __str__(self):
        """
        Виводить інформацію про замовлення.
        """
        items_str = "\n".join([f"{item.name}: {cnt} pcs." for item, cnt in self.products.items()])
        return f"User: {self.user}\nItems:\n{items_str}"


# Створення екземплярів класів
lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

buyer = User("Ivan", "Ivanov", "02628162")

cart = Purchase(buyer)

# Перевірка: чи є cart.user екземпляром User
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'

# Додаємо товари до кошика
cart.add_item(lemon, 4)
cart.add_item(apple, 20)

# Перевірка початкової загальної вартості
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'

# Виведення поточного стану кошика
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

# Додаємо ще одну партію товару
cart.add_item(apple, 10)

# Виведення оновленого стану кошика
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 30 pcs.
"""