# ООП - 2



# Множественное наследование и Mixin-классы
# Mixin классы - это классы у которых нет данных, но есть методы.
# Класс Flyer, содержащий метод fly
class Flyer:
    def fly(self):
        print("Летать")  # Реализация метода fly

# Класс Swimmer, содержащий метод swim
class Swimmer:
    def swim(self):
        print("Плавать")  # Реализация метода swim

# Класс Duck, наследующийся от Flyer и Swimmer - множественное наследование
class Duck(Flyer, Swimmer):
    def quack(self):
        print("Кря-кря")  # Реализация метода quack

# Создание объекта класса Duck
duck = Duck()  # Создаем объект duck класса Duck

# Вызов методов, унаследованных от Flyer и Swimmer, а также собственного метода quack
duck.fly()  # Вывод: Летать, метод из класса Flyer
duck.swim()  # Вывод: Плавать, метод из класса Swimmer
duck.quack()  # Вывод: Кря-кря, метод из класса Duck




# Декораторы классов
# Функция add_greeting принимает класс cls в качестве аргумента. Внутри функции мы добавляем новый атрибут greeting к классу cls со значением "Привет!". Затем функция возвращает измененный класс cls.
def add_greeting(cls):
    cls.greeting = "Привет!"  # Добавляем атрибут greeting со значением "Привет!"
    return cls  # Возвращаем измененный класс

# Применяем декоратор add_greeting к классу Person, это эквивалентно вызову Person = add_greeting(Person), что добавляет атрибут greeting к классу Person.
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name  # Атрибут name экземпляра класса

# Создание объекта класса Person
person = Person("Иван")  # Создаем объект person с именем "Иван"

# Доступ к атрибуту greeting, добавленному декоратором
print(person.greeting)  # Вывод: Привет!




# Статические методы и методы класса
# Класс MathOperations, содержащий статический метод add и метод класса multiply
class MathOperations:
    def __init__(self):
        self.pi = 3.14 # переменная доступная всему классу 
    # @staticmethod - декоратор, который определяет метод add как статический. Статические методы не требуют доступа к экземпляру класса (self), и их можно вызывать через имя класса.
    @staticmethod
    def add(x, y):
        # self.pi - нет доступа к переменным класса
        return x + y  # Статический метод для сложения двух чисел

    # @classmethod - декоратор, который определяет метод multiply как метод класса. Методы класса имеют доступ к классу (cls) в качестве первого аргумента и могут использоваться для работы с классовыми переменными.
    @classmethod
    def multiply(cls, x, y):
        cls.pi = 3.14159 # есть доступ к переменным класса
        return x * y  # Метод класса для умножения двух чисел

# Вызов статического метода add через имя класса
print(MathOperations.add(3, 5))  # Вывод: 8, результат сложения 3 и 5

# Вызов метода класса multiply через имя класса
print(MathOperations.multiply(4, 6))  # Вывод: 24, результат умножения 4 и 6




# Пример
# Класс Rectangle, представляющий прямоугольник
class Rectangle:
    def __init__(self, width, height):
        self.width = width  # Атрибут width экземпляра класса, хранящий ширину прямоугольника
        self.height = height  # Атрибут height экземпляра класса, хранящий высоту прямоугольника

    def area(self):
        return self.width * self.height  # Метод для вычисления площади прямоугольника

# Создание объектов класса Rectangle с различными размерами
rect1 = Rectangle(4, 5)  # Создаем объект rect1 с шириной 4 и высотой 5
rect2 = Rectangle(7, 3)  # Создаем объект rect2 с шириной 7 и высотой 3

# Вычисление и вывод площади каждого из прямоугольников
print(rect1.area())  # Вывод: 20, площадь прямоугольника rect1
print(rect2.area())  # Вывод: 21, площадь прямоугольника rect2




# Композиция
# Класс Engine, представляющий двигатель
class Engine:
    def start(self):
        print("Двигатель запущен")

# Класс Car, использующий композицию для включения объекта Engine
class Car:
    def __init__(self):
        self.engine = Engine()  # Создаем объект Engine внутри класса Car

    def start_engine(self):
        self.engine.start()  # Вызываем метод start() у объекта Engine

# Создание объекта класса Car и запуск двигателя через композицию
car = Car()
car.start_engine()  # Вывод: Двигатель запущен




# Агрегация
# Класс Passenger, представляющий пассажира
class Passenger:
    def __init__(self, name):
        self.name = name  # Имя пассажира

# Класс Car с агрегацией объектов Passenger
class Car:
    def __init__(self, passengers=[]):
        self.passengers = passengers  # Список пассажиров

    def add_passenger(self, passenger):
        self.passengers.append(passenger)  # Добавляем пассажира в список

# Создаем объекты пассажиров и добавляем их в объект автомобиля
passenger1 = Passenger("Анна")
passenger2 = Passenger("Петр")

car = Car()
car.add_passenger(passenger1)
car.add_passenger(passenger2)

for passenger in car.passengers:
    print(passenger.name)  # Вывод: Анна, Петр




# Наследование и метод super()
# Базовый класс Vehicle
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_info(self):
        print(f"Марка: {self.brand}")

# Подкласс Car, наследующийся от Vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Вызываем конструктор родительского класса
        self.model = model

    def show_info(self):  # Переопределяем метод show_info()
        super().show_info()  # Вызываем метод show_info() родительского класса
        print(f"Модель: {self.model}")

# Создание объекта класса Car и вызов метода show_info()
car = Car("Toyota", "Camry")
car.show_info()
# Вывод:
# Марка: Toyota
# Модель: Camry