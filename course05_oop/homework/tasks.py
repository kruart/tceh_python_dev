# *ЗАДАЧА 1:
# Реализовать класс Person, у которого должно быть два публичных поля: age и name.
# Также у него должен быть следующий набор методов: know(person), который позволяет
# добавить другого человека в список знакомых. И метод is_known(person), который возвращает знакомы ли два человека
class Person:

    def __init__(self, name: str, age: int) -> None:
        self.familiars = []
        self.name = name
        self.age = age

    def know(self, person) -> None:
        if person not in self.familiars:
            self.familiars.append(person)
            print('{} is added to {} friend list'.format(person.name, self.name))
        else:
            print('{} is already in your friend list')

    def is_known(self, person) -> bool:
        return person in self.familiars


arthur = Person('Arthur', 27)
kevin = Person('Kevin', 25)

print(kevin.is_known(arthur))
kevin.know(arthur)
print(kevin.is_known(arthur))


# *ЗАДАЧА 2:
# Есть класс, который выводит информацию в консоль: Printer, у него есть метод: log(*values).
# Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *
class Printer:
    def log(self, * values):
        print(values)


class FormattedPrinter(Printer):
    def log(self, *values):
        print('****************')
        super().log(*values)
        print('****************')


a = Printer()
a.log(1, 2, 3, 4, 5, 6, 7, 8, 9)

b = FormattedPrinter()
b.log(1, 2, 3, 4, 5, 6, 7, 8, 9)


# *ЗАДАЧА 3:
# Написать класс Animal и Human,сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
# Другие - нет. За что будет отвечать метод is_dangerous(animal)
class Animal:
    def __init__(self, name: str, is_predator, is_poisonous) -> None:
        self.name = name
        self.is_predator = is_predator
        self.is_poisonous = is_poisonous


class Human:
    def is_dangerous(self, animal) -> bool:
        return animal.is_predator or animal.is_poisonous


human = Human()
tiger = Animal('tiger', True, False)
snake = Animal('snake', False, True)
rabbit = Animal('rabbit', False, False)

print(human.is_dangerous(tiger))
print(human.is_dangerous(snake))
print(human.is_dangerous(rabbit))
