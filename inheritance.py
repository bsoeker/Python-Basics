class Animal:
    def eat(self):
        print("eating!?")


class Mammal(Animal):
    def walk(self):
        print("Glamorous walking!")


class Fish(Animal):
    def swim(self):
        print("Swimming...")


horse = Mammal()
horse.eat()
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
