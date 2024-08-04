print('Домашнее задание по теме "Зачем нужно наследование"')
print('Задача "Съедобное, несъедобное":')
print('Студент Крылов Эдуард Васильевич')
thanks = 'Благодарю за внимание :-)'
print()


class Animal:
    def __init__(self, name: str):
        self.name = name
        self.alive = True
        self.fed = False


class Plant:
    def __init__(self, name: str):
        self.name = name
        self.edible = False


class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name}, съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name}, не стал есть {food.name}')
            self.alive = False


class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name}, съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name}, не стал есть {food.name}')
            self.alive = False


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


# Выполняемый код(для проверки):
a1 = Predator('Хищник: Волк с Уолл-Стрит')
a2 = Mammal('Млекопитающее: Хатико')
# a3 = Predator('Эдисон')

p1 = Flower('Цветок: Цветик семицветик')
p2 = Fruit('Фрукт: Заводной апельсин')

print(a1.name)
print(p1.name)

print(f'Хищник живой: {a1.alive}')
print(f'Млекопитающее покормил: {a2.fed}')
a1.eat(p1)
a2.eat(p2)
print(f'Живой: {a1.alive}')
print(f'Покормил: {a2.fed}')

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
print()
print(thanks)
