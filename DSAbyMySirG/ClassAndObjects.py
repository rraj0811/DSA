# class Test:
#     x = 5
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def show(self):
#         print(self.a, self.b)

#     @staticmethod
#     def f2():
#         print("Hello Static Method")  

#     @classmethod
#     def f3(cls):
#         print(cls.x) 

# t1 = Test(2, 3)
# t2 = Test(5, 6)
# t1.show() 
# ## Static Method Call 
# # t1.f2()
# # Test.f2()

# ## Class Method Call
# # Test.f3()
# # t1.f3()


class Employee:
    def __init__(self, empid=None, name=None, salary=None) -> None:
        self.empid = empid
        self.name = name
        self.salary = salary
    
    def setEmpid(self, empid):
        self.empid = empid
    def setName(self, name):
        self.name = name
    def setSalary(self, salary):
        self.salary = salary

    def getEmpid(self):
        return self.empid
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    
e1 = Employee()
e2 = Employee(1, "Rahul", 40000)
e1.setEmpid(2)
e1.setName("Romesh")
e1.setSalary(50000)
print(e1.getEmpid(), e1.getName(), e1.getSalary())
print(e2.getEmpid(), e2.getName(), e2.getSalary())


    
