class GroupLimitError(Exception):
    """
    Виняток для перевищення ліміту студентів у групі.
    """
    def __init__(self, message="У групі не може бути більше 10 студентів."):
        super().__init__(message)


class Human:
    """
    Клас, що описує людину.
    """

    def __init__(self, gender, age, first_name, last_name):
        """
        Ініціалізація об'єкта людини.
        :param gender: Стать людини.
        :param age: Вік людини.
        :param first_name: Ім'я.
        :param last_name: Прізвище.
        """
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        """
        Повертає інформацію про людину.
        """
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} років"


class Student(Human):
    """
    Клас, що описує студента, на основі класу Human.
    """

    def __init__(self, gender, age, first_name, last_name, record_book):
        """
        Ініціалізація об'єкта студента.
        :param record_book: Номер залікової книжки.
        """
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        """
        Повертає інформацію про студента.
        """
        return f"{super().__str__()}, Залікова книжка: {self.record_book}"


class Group:
    """
    Клас, що описує групу студентів.
    """

    def __init__(self, number):
        """
        Ініціалізація об'єкта групи.
        :param number: Назва або номер групи.
        """
        self.number = number
        self.group = set()

    def add_student(self, student):
        """
        Додає студента до групи.
        :param student: Екземпляр класу Student.
        :raises GroupLimitError: Якщо кількість студентів перевищує 10.
        """
        if len(self.group) >= 10:
            raise GroupLimitError()
        self.group.add(student)

    def find_student(self, last_name):
        """
        Шукає студента за прізвищем.
        :param last_name: Прізвище студента.
        :return: Екземпляр Student або None, якщо студент не знайдений.
        """
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        """
        Видаляє студента за прізвищем.
        :param last_name: Прізвище студента.
        """
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        """
        Повертає список студентів у вигляді рядка.
        """
        all_students = "\n".join(str(student) for student in self.group)
        return f"Група: {self.number}\n{all_students}"


# Тестування
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')

# Додавання студентів
try:
    gr.add_student(st1)
    gr.add_student(st2)
    # Додаємо більше студентів для перевірки
    for i in range(3, 12):
        gr.add_student(Student('Male', 20 + i, f'Student{i}', f'LastName{i}', f'AN{i}'))
except GroupLimitError as e:
    print(e)

# Виведення інформації про групу
print(gr)

# Тести на пошук студента
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку має повертати екземпляр'

# Видалення студентів
gr.delete_student('Taylor')
print(gr)  # Лише залишились інші студенти

# Спроба видалення неіснуючого студента
gr.delete_student('Taylor')  # Не повинно бути помилок

