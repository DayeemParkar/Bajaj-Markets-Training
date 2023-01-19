'''This file contains the department class'''

class Dept:
    def __init__(self, dname):
        self.__dname = dname
    
    def getDeptName(self):
        return self.__dname
    
    pass
