# # # # # # # n1=int(input("Enter number 1: "))
# # # # # # # n2=int(input("Enter number 2: "))
# # # # # # # n3=int(input("Enter number 3: "))
# # # # # # # def greatest(n1,n2,n3):
# # # # # # #     if(n1>n2 and n1>n3):
# # # # # # #         print(n1,"is greatest number.")
# # # # # # #     elif(n2>n3):
# # # # # # #         print(n2,"is greatest number.")
# # # # # # #     else:
# # # # # # #         print(n3,"is a greatest number.")
# # # # # # # greatest(n1,n2,n3)

# # # # # # t=int(input("Enter temperature in celcius: "))
# # # # # # def faranhit(t):
# # # # # #     return t*(9/5)+32
# # # # # # print("The temperature in feranhit is :",faranhit(t))

# # # # # # --> To prevent print() function to add new line at the end use end="" 

# # # # # n=int(input("Enter a number "))
# # # # # def sum(n):
# # # # #     if n==1:
# # # # #         return 1
# # # # #     elif n==0:
# # # # #         return 0
# # # # #     else:
# # # # #         return n+sum(n-1)
# # # # # print("The sum of n number is ",sum(n))
# # # # #--> If you enter 1000 number in input it shoes error which says maximum space is aquired by recursion. So use visely

# # # # n=80
# # # # for i in reversed(range(n)):
# # # #     print("* "*(i+1))
    
# # # n=float(input("Enter length in inches: "))
# # # def cm(n):
# # #     return n*2.54
# # # print("The length in cm is ",cm(n))

# # n=int(input("Enter a number: "))
# # def multi(n):
# #     for i in range(10):
# #      print(f"{n} X {i+1} = {n*i}")
# # multi(n)

# l1=["vinit","dipen","kirtan","hardik"]
# def addremove(n1,n2):
#     l1.remove(n1)
#     l1.append(n2)
#     print(l1)
# print(l1)
# n1=input("Enter a name you want to remove: ")
# n2=input("Enter a name you want to add: ")
# addremove(n1,n2)