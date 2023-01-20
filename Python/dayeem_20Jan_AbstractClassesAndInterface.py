from abc import ABC, abstractmethod
# ABC stands for abstract base classes

# interface
class MyClass(ABC):
    def connect(self):
        pass
    
    def disconnect(self):
        pass


class MainClass(ABC):
    @abstractmethod
    def calc(self, x):
        pass


class SubClass(MainClass):
    def calc(self, x):
        print('Square:', x ** 2)


if __name__ == '__main__':
    ob = SubClass()
    ob.calc(10)
