class Counter:
    """
    Клас для цифрового лічильника з можливістю встановлення мінімального, максимального та початкового значень.
    """

    def __init__(self, current=1, min_value=0, max_value=10):
        """
        Ініціалізація лічильника.
        :param current: Початкове значення лічильника.
        :param min_value: Мінімальне значення лічильника.
        :param max_value: Максимальне значення лічильника.
        :raises ValueError: Якщо початкове значення виходить за межі [min_value, max_value].
        """
        if not (min_value <= current <= max_value):
            raise ValueError("Initial value must be between min_value and max_value")
        self.current = current
        self.min_value = min_value
        self.max_value = max_value


    def set_current(self, start):
        """
        Встановлення поточного значення лічильника.
        :param start: Нове поточне значення.
        :raises ValueError: Якщо значення виходить за межі [min_value, max_value].
        """
        if not (self.min_value <= start <= self.max_value):
            raise ValueError("Current value must be between min_value and max_value")
        self.current = start


    def set_max(self, max_max):
        """
        Встановлення максимального значення лічильника.
        :param max_max: Нове максимальне значення.
        :raises ValueError: Якщо нове максимальне значення менше мінімального.
        """
        if max_max < self.min_value:
            raise ValueError("Maximum value must be greater than min_value")
        self.max_value = max_max
        # Якщо поточне значення перевищує нове максимальне, обмежуємо його
        if self.current > self.max_value:
            self.current = self.max_value


    def set_min(self, min_min):
        """
        Встановлення мінімального значення лічильника.
        :param min_min: Нове мінімальне значення.
        :raises ValueError: Якщо нове мінімальне значення більше максимального.
        """
        if min_min > self.max_value:
            raise ValueError("Minimum value must be less than max_value")
        self.min_value = min_min
        # Якщо поточне значення нижче нового мінімального, обмежуємо його
        if self.current < self.min_value:
            self.current = self.min_value


    def step_up(self):
        """
        Збільшення поточного значення лічильника на 1.
        :raises ValueError: Якщо поточне значення вже досягло максимального.
        """
        if self.current >= self.max_value:
            raise ValueError("Maximum value reached")
        self.current += 1


    def step_down(self):
        """
        Зменшення поточного значення лічильника на 1.
        :raises ValueError: Якщо поточне значення вже досягло мінімального.
        """
        if self.current <= self.min_value:
            raise ValueError("Minimum value reached")
        self.current -= 1


    def get_current(self):
        """
        Повертає поточне значення лічильника.
        :return: Поточне значення.
        """
        return self.current


# Тестування
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Досягнуто максимума
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Досягнуто минимума
assert counter.get_current() == 7, 'Test4'
