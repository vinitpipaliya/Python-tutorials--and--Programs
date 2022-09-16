# class C2_dVector:
#     def __init__(self,i,j) :
#         self.icap=i
#         self.jcap=j
#     def __str__(self) :
#         return f"{self.icap}i + {self.jcap}j"                
# class C3_dVector(C2_dVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.kcap=k
#     def __str__(self) -> str:
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
# a=C2_dVector(1,3)
# b=C3_dVector(1,5,9)
# print(a)
# print(b)

# class Animals:
#     AnimalType="Mammal"
# class Pets:
#     color="White"
# class Dog:
#     @staticmethod
#     def bark():
#         print("Bhau Bhau")
# Tommy=Dog()
# Tommy.bark()

# class Employee:
#     salary=1000
#     increment=1.5
#     @property
#     def salaryAfterIncrement(self):
#         return self.salary*self.increment
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,sai):
#         self.increment=sai/self.salary
# e=Employee()
# print(e.salaryAfterIncrement)
# print(e.increment)
# e.salaryAfterIncrement=2000
# print(e.increment)

# (a+bi)(c+di) = (ac−bd) + (ad+bc)i
# class Complex:
#     def __init__(self,r,i):
#         self.real=r
#         self.imaginary=i
#     def __add__(self,c):
#         return Complex(self.real+c.real,self.imaginary+c.imaginary)
#     def __mul__(self,c):
#         mulReal=self.real*c.real-self.imaginary*c.imaginary
#         mulImg=self.real*c.imaginary-self.imaginary*c.real
#         return Complex(mulReal,mulImg)
#     def __str__(self) :
#         if self.imaginary<0:
#             return f"{self.real}-{-self.imaginary}i"
#         else:
#             return f"{self.real}+{self.imaginary}i"        
# c1=Complex(1,-34)
# c2=Complex(4,-8)
# print(c1+c2)
# print(c1*c2)

# class Vector:
#     def __init__(self,vec):
#         self.vec=vec
#     def __str__(self):
#         str1=""
#         index=0
#         for i in self.vec:
#             str1+=f" {i}a{index} +"
#             index+=1
#         return str1[:-1]
#     def __add__(self,vec2):
#         newList=[]
#         for i in range(len(self.vec)):
#             newList.append(self.vec[i]+vec2.vec[i])
#         return Vector(newList)
#     def __mul__(self,vec2):
#         sum=0
#         for i in range(len(self.vec)):
#             sum+=self.vec[i]*vec2.vec[i]
#         return sum
# v1=Vector([1,4,7])
# v2=Vector([1,3,5])
# print(v1+v2)
# print(v1*v2)

# class Vector:
#     def __init__(self,vec):
#         self.vec=vec
#     def __str__(self):
#         return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
# v1=Vector([1,2,3])    
# print(v1)   

# class Vector:
#     def __init__(self,vec):
#         self.vec=vec
#     def __str__(self):
#         str1=""
#         index=0
#         for i in self.vec:
#             str1+=f" {i}a{index} +"
#             index+=1
#         return str1[:-1]
#     def __add__(self,vec2):
#         newList=[]
#         for i in range(len(self.vec)):
#             newList.append(self.vec[i]+vec2.vec[i])
#         return Vector(newList)
#     def __mul__(self,vec2):
#         sum=0
#         for i in range(len(self.vec)):
#             sum+=self.vec[i]*vec2.vec[i]
#         return sum
#     def __len__(self):
#         return len(self.vec)
# v1=Vector([1,4,7.3,4,6,7])
# v2=Vector([1,3,5])
# print(len(v1)) 
# print(len(v2) )

# import collections
# class Vector:
#     def __init__(self,vec):
#         self.vec=vec
#     def __str__(self):
#         str1=""
#         index=0
#         for i in self.vec:
#             str1+=f"{i}a{index} +"
#             index+=1
#         return str1[:-1]
#     def __add__(self,vec2):
#         newList=[]
#         if collections.Counter(self.vec)==collections.Counter(vec2.vec):
#             for i in range(len(self.vec)):
#                 newList.append(self.vec[i]+vec2.vec[i])
#             return Vector(newList)
#         else :
#             print("Addition is not Possible")
#     def __mul__(self,vec2):
#         sum=0
#         if len(self.vec)!=len(vec2.vec):
#             print("Multiplication is not Posiible")
#         else:
#             for i in range(len(self.vec)):
#                 sum+=self.vec[i]*vec2.vec[i]
#             return sum
# v1=Vector([1,3,5,3])
# v2=Vector([1,7,9])
# print(v1+v2)
# print(v1*v2)