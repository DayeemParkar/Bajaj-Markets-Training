from dayeem_19Jan_dept import Dept

class Emp:
    org = 'Bajaj Markets' # class variable shared by all objects
    def __init__(self, eid, ename, esal=60000, dept=None):
        self.eid = eid
        self.ename = ename
        self.esal = esal
        self.dept = dept
    
    def disp(self):
        print("ID:", self.eid, "| Name:", self.ename, "| Salary:", self.esal, '| Department:', self.dept._Dept__dname, '| Org:', Emp.org)
    
    @staticmethod
    def staticDemo(newOrg):
        Emp.org = newOrg
    
    @classmethod
    def modifyOrg(cls, newOrg):
        cls.org = newOrg


if __name__ == '__main__':
    emp1 = Emp(1,'Dayeem', 60000, Dept('Python'))
    emp2 = Emp(2,'Shivam', 60000, Dept('Python Micro'))
    emp3 = Emp(3,'Adithya', 60000, Dept('Python'))
    
    # modify all objects except those that have explicitly changed class var
    emp1.modifyOrg('Bajaj modified')
    print(emp1.org, '|', emp2.org, '|', emp3.org)

    # modify for specific object
    emp2.org = 'Bajaj specific modified'
    print(emp1.org, '|', emp2.org, '|', emp3.org)

    # modify all objects except those that have explicitly changed class var
    Emp.staticDemo('Bajaj all modified')
    print(emp1.org, '|', emp2.org, '|', emp3.org)

    emp2.staticDemo('Bajaj all modified again')
    print(emp1.org, '|', emp2.org, '|', emp3.org)
    
    # emp1.disp()
    # emp2.disp()
