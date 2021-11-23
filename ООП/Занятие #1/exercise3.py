class Nikola:
    __slots__ = ['name', 'age']
    def __init__(self, name, age):
        self.name = name
        self.age = age
        if self.name != 'Николай':
            self.name = f'Я не {self.name}, а Николай'


person1 = Nikola('Иван', 31)
person2 = Nikola('Николай', 14)
print(person1.name)
print(person2.name)
person2.surname = 'Петров'