# class Employee:
#     company="Google"
#     def __init__(self) :
#         print("This is base class")
        
#     def showdata(self):
#         print("This is Employee class")
#     def facility(self):
#         print("This is Facility method")

# class Nationality(Employee):
#     def __init__(self):
#         super().__init__()
#         print("This is derived class")
#     def Adharcard(self):
#         print("This is nationality")
    
# class Programmer(Nationality):
#     company="Google LLC"
#     def __init__(self):
#         super().__init__()
#         print("This is also derived class")
#     def showdata(self) :
#         print("This is Programmer class")
  

# p=Programmer()
# # p.showdata()
# # p.facility()
# # p.Adharcard()


# class Employee:
#     company="Google"
#     salary=1000
#     id=129045
#     @classmethod
#     def changesalary(cls,newsal):
#         cls.salary=newsal
# e=Employee
# print(e.salary)
# e.changesalary(1200)
# print(e.salary)


# class Employee:
#     compnay="Google"
#     salary=1000
#     salarybonus=400
#     @property
#     def totalsalary(self): #-->This is getter
#         return self.salary + self.salarybonus
#     @totalsalary.setter
#     def totalsalary(self,value):
#         self.salarybonus=value-self.salary
# e=Employee()
# print(e.totalsalary)
# e.totalsalary=2000
# print(e.salary)
# print(e.salarybonus)


# from operator import floordiv, truediv


# class Number:
#     def __init__(self,num) :
#         self.num=num
#     def __add__(self, num2):
#         print("Lets add")
#         return self.num + num2.num
#     def __mul__(self,num2):
#         print("Multiplication")
#         return self.num * num2.num
#     def __sub__(self,num2):
#         print("Multiplication")
#         return self.num - num2.num
#     def __truediv__(self,num2):
#         print("Multiplication")
#         return self.num / num2.num
#     def __floordiv__(self,num2):
#         print("Multiplication")
#         return self.num // num2.num
#     def __str__(self):
#         return f"Decimnal Number is {self.num}"
#     def __len__(self):
#         return 1
    
# n1=Number(109090)
# print(n1)
# print(len(n1))
# n2=Number(20)
# sum = n1 + n2
# print(sum)
# mul= n1 * n2
# print(mul)
# sub=n1-n2
# print(sub)
# truediv=n1/n2
# print(truediv)
# floordiv=n1//n2
# print(floordiv)