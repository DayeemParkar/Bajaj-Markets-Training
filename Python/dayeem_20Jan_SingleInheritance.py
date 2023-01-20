class Student:
    def __init__(self, name, age):
        self.n = name
        self.a = age
    
    def getStudentInfo(self):
        return self.n, self.a
    
    def setStudentInfo(self, name, age):
        self.n = name
        self.a = age


class ScienceStudent(Student):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def getSubj(self):
        return 'Science'


if __name__ == '__main__':
    s1 = ScienceStudent('Dayeem', 21)
    print(s1.getStudentInfo())
    s1.setStudentInfo('Dayeem2', 500)
    print(s1.getStudentInfo())
    print(s1.getSubj())
