import datetime

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    
    # actual obj string format
    def __repr__(self):
        return f'(Person name={self.name}, pay={self.pay})'
    
    # readable string format
    def __str__(self):
        return f'(Person with name={self.name} and pay={self.pay})'
    
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, perc):
        self.pay = int(self.pay * (1 + perc / 100))

bob = Person('Bob Smith', pay=500)
she = Person('She Jones', job='Dev', pay=100000)
bob.giveRaise(20)
print(bob.lastName() + ' pay:', bob.pay)


now = datetime.datetime.now()
print('\n' + now.__str__())
print(now.__repr__())

print('\n' + bob.__str__())
print(bob.__repr__())
