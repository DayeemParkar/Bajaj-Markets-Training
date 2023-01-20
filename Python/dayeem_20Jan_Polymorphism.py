class Cat:
    def __init__(self, name, age):
        self.n = name
        self.a = age
    
    def info(self):
        print(f'I am cat. My name is {self.n} and age is {self.a}')
    
    def speak(self):
        print('meow')


class Dog:
    def __init__(self, name, age):
        self.n = name
        self.a = age
    
    def info(self):
        print(f'I am dog. My name is {self.n} and age is {self.a}')
    
    def speak(self):
        print('woof')


if __name__ == '__main__':
    cat = Cat('Sadie', 5)
    dog = Dog('Pete', 7)
    for animal in (cat, dog):
        animal.info()
        animal.speak()
