class Animal:
    def __init__(self, animal):
        self.a = animal
        print(self.a, 'is an animal')


class Mammal(Animal):
    def __init__(self, mammal):
        print(mammal, 'is a mammal')
        super().__init__(mammal)


class NonWinged(Mammal):
    def __init__(self, nonwinged):
        print(nonwinged, 'cant fly')
        super().__init__(nonwinged)


class NonMarineMammal(Mammal):
    def __init__(self, nonmarine):
        print(nonmarine, 'cant swim')
        super().__init__(nonmarine)

class Dog(NonWinged, NonMarineMammal):
    def __init__(self, dog):
        print(dog, 'is a dog')
        super().__init__(dog)


if __name__ == '__main__':
    dog = Dog('Dog')
    print(Dog.mro())

