class Employee:
    company="My"
    
    def __init__(self,name,salary):
        print("Welcomre to Python")
        self.salary=100
        self.name=name

    def getsalary(self):
        print(f"Salary of {self.name} is {self.salary}")

    @staticmethod
    def greet():
        print("Namaste")

    
vinit=Employee("vinit","100000")
vinit.getsalary()
# vinit.name="vinit"
# print(vinit.company)
# print(vinit.salary)
# vinit.salary=100000
# print(vinit.salary)
# vinit.getsalary()
# vinit.greet()