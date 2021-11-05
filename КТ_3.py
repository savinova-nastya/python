from dataclasses import dataclass
from random import randint


class Family:
    def __init__(self, name: str, quantity: int):
        self.__name = name  # имя
        self.__quantity = quantity  # количество

    @property
    def name(self):
        return self.__name

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        try:
            quantity = int(quantity)
            if quantity < 0:
                raise CustomError('Вы ввели отрицательное количество!')
            else:
                self.__quantity = quantity
        except ValueError:
            print('Ошибка при вводе количества, ввели не число')
        except CustomError as msg:
            print(msg)

    def display_info(self):
        print('Семья:', self.__name, 'В количестве:', self.__quantity)

    def __str__(self):
        return "Наименование: {} \t Количество: {}".format(self.__name, self.__quantity)

    def __eq__(self, other):
        if type(self) == type(other):
            return self.__quantity == other.quantity
        else:
            print('Невозможно сравнить')
            return False

    def __add__(self, other):
        return self.__quantity + other

    def __sub__(self, other):
        return self.__quantity - other


class Sis(Family):
    # конструктор
    def __init__(self, name, quantity, town: str):
        Family.__init__(self, name, quantity)
        self.town = town

    # переопределим метод
    def display_info(self):
        print('Сестра', 'в количестве:', self.quantity, 'из города:', self.town)


class Bro(Family):
    # конструктор
    def __init__(self, name, quantity, shape: str):
        Family.__init__(self, name, quantity)
        self.shape = shape

    def display_info(self):
        print('Братья', 'в количестве:', self.quantity, 'из страны:', self.shape)


# дата класс
@dataclass
class Fam:
    sis_qty: int
    bro_qty: int


# пользовательское исключение
class CustomError(Exception):
    def __init__(self, text):
        self.txt = text


# создаем экземпляры классов
family = Family('Какая-то семья', 1)
bro = Bro('Джон', 1, 'Англия')
another_bro = Bro('Степан', 1, 'Россия')
sis = Sis('Мария', 1, 'Пермь')
# сравниваем экземпляры классов
print(family == bro)
print(family == family)
# переопределяем метод __str__
print(bro)
# используем свойства у экземпляров классов
bro.display_info()
family.display_info()
# дата класс
fam = Fam(bro.quantity, sis.quantity)
print(fam)

# Определяем пользовательское исключение
family_new = Family("Другая семья", 2);
family_new.quantity = 5
family_new.quantity = 'asd'
print(family_new)


# Генератор брата
def random_round_bro(quantity):
    while quantity > 0:
        quantity -= 1
        yield Bro("Стас", randint(1, 4), "Америка")


generator = random_round_bro(3)
for i in generator:
    print(i.display_info())
