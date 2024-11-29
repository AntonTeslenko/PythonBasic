from math import gcd  # Імпортуємо функцію для знаходження найбільшого спільного дільника (НСД)

class Fraction:
    # Ініціалізуємо клас "Правильний дріб" з чисельником 'a' та знаменником 'b'
    def __init__(self, a, b):
        # Перевіряємо, чи знаменник не є нулем
        if b == 0:
            raise ValueError("Знаменник не може бути нулем")  # Якщо знаменник 0, викидаємо помилку
        self.a = a  # Чисельник
        self.b = b  # Знаменник
        self._simplify()  # Викликаємо метод для спрощення дробу після ініціалізації

    # Допоміжний метод для спрощення дробу
    def _simplify(self):
        # Знаходимо найбільший спільний дільник (НСД) чисельника та знаменника
        common_divisor = gcd(self.a, self.b)
        self.a //= common_divisor  # Спрощуємо чисельник
        self.b //= common_divisor  # Спрощуємо знаменник

        # Якщо знаменник від'ємний, переносимо знак на чисельник
        # Це робимо для того, щоб дроби завжди мали від'ємний знак в чисельнику, а не в знаменнику
        if self.b < 0:
            self.a = -self.a
            self.b = -self.b

    # Метод для множення двох дробів
    def __mul__(self, other):
        # Перевіряємо, чи інший об'єкт також є екземпляром класу Fraction
        if isinstance(other, Fraction):
            # Множимо чисельники та знаменники між собою
            return Fraction(self.a * other.a, self.b * other.b)
        return NotImplemented  # Якщо об'єкт не є дробом, повертаємо NotImplemented

    # Метод для додавання двох дробів
    def __add__(self, other):
        # Перевіряємо, чи інший об'єкт також є екземпляром класу Fraction
        if isinstance(other, Fraction):
            # Приводимо дроби до спільного знаменника
            common_denominator = self.b * other.b
            # Вираховуємо новий чисельник, з урахуванням спільного знаменника
            numerator = self.a * other.b + other.a * self.b
            return Fraction(numerator, common_denominator)  # Створюємо новий дріб з результатом
        return NotImplemented  # Якщо об'єкт не є дробом, повертаємо NotImplemented

    # Метод для віднімання двох дробів
    def __sub__(self, other):
        # Перевіряємо, чи інший об'єкт є екземпляром класу Fraction
        if isinstance(other, Fraction):
            # Приводимо дроби до спільного знаменника
            common_denominator = self.b * other.b
            # Вираховуємо новий чисельник для віднімання
            numerator = self.a * other.b - other.a * self.b
            return Fraction(numerator, common_denominator)  # Створюємо новий дріб з результатом
        return NotImplemented  # Якщо об'єкт не є дробом, повертаємо NotImplemented

    # Метод для порівняння двох дробів на рівність
    def __eq__(self, other):
        # Перевіряємо, чи інший об'єкт є екземпляром класу Fraction
        if isinstance(other, Fraction):
            # Перевіряємо, чи дроби рівні, порівнюючи їх після приведення до спільного знаменника
            return self.a * other.b == self.b * other.a
        return NotImplemented  # Якщо об'єкт не є дробом, повертаємо NotImplemented

    # Метод для порівняння, чи один дріб більший за інший
    def __gt__(self, other):
        # Перевіряємо, чи інший об'єкт є екземпляром класу Fraction
        if isinstance(other, Fraction):
            # Порівнюємо дроби, перехресно множачи чисельники і знаменники
            return self.a * other.b > self.b * other.a
        return NotImplemented  # Якщо об'єкт не є дробом, повертаємо NotImplemented

    # Метод для порівняння, чи один дріб менший за інший
    def __lt__(self, other):
        # Перевіряємо, чи інший об'єкт є екземпляром класу Fraction
        if isinstance(other, Fraction):
            # Порівнюємо дроби, перехресно множачи чисельники і знаменники
            return self.a * other.b < self.b * other.a
        return NotImplemented  # Якщо об'єкт не є дробом, повертаємо NotImplemented

    # Метод для виведення дробу у вигляді рядка
    def __str__(self):
        # Повертаємо рядкове представлення дробу
        return f"{self.a}/{self.b}"

# Тестування

# Створюємо два дроби
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

# Тест на додавання дробів
f_c = f_b + f_a
# Перевіряємо, чи додавання працює правильно (3/6 + 2/3 = 7/6)
assert str(f_c) == '7/6', f"Помилка в додаванні: {f_c}"

# Тест на множення дробів
f_d = f_b * f_a
# Перевіряємо, чи множення працює правильно (3/6 * 2/3 = 6/18, спрощується до 1/3)
assert str(f_d) == '1/3', f"Помилка в множенні: {f_d}"

# Тест на віднімання дробів
f_e = f_a - f_b
# Перевіряємо, чи віднімання працює правильно (2/3 - 3/6 = 3/18, спрощується до 1/6)
assert str(f_e) == '1/6', f"Помилка в відніманні: {f_e}"

# Тест на порівняння дробів
assert f_d < f_c  # Перевіряємо, чи 1/3 менше за 7/6
assert f_d > f_e  # Перевіряємо, чи 1/3 більше за 1/6
assert f_a != f_b  # Перевіряємо, чи 2/3 не дорівнює 3/6

# Рівність дробів (спрощення)
f_1 = Fraction(2, 4)  # Це буде спрощено до 1/2
f_2 = Fraction(3, 6)  # Це буде спрощено до 1/2
# Перевіряємо, чи дроби рівні після спрощення
assert f_1 == f_2  # True

print("OK")  # Якщо всі тести проходять, виводимо "OK"

