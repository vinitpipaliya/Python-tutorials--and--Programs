# n=int(input("Enter a number: "))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)
#     i=i+1

# l1=["harry","sohan","sachin","rahul"]
# for name in l1:
#     # if name=="sohan" or name=="sachin":
#     if name.startswith("s"):
#         print("Good morning,",name)

# n=int(input("Enter a number: "))
# i=1
# while(i<=10):
#     # print(n,"*",i,"=",n*i)
#     print(f"{n} X {i} = {n*i}")
#     i=i+1

# n=int(input("Enter a number: "))
# for i in range(2,n-1):
#     if(n%i==0):
#         print(n,"is not prime number")
#         break
#     else:
#         print(n,"is prime number")
#         break

# n=int(input("Enter a number: "))
# i=1
# s=0
# while(i<=n):
#     s=s+i
#     i=i+1
# print("Sum of",n,"natural number is ",s)

# n=int(input("Enter a number: "))
# f=1
# for i in range(1,n+1):
#     f=f*i
#     i=i+1
# print("Factorial of",n,"number is",f)

# n=int(input("How many line do you want to print: "))
# for i in range(1,n+1):
#     for j in range(1,n+3):
#         if(j>=(4-i) and j<=(2+i)):
#             print("* ",end=" ")
#         else:
#             print("  ",end=" ")
#     print("\n")
# n = 3
# for i in range(3): 
#     print(" " * (n-i-1), end="")
#     print("*" * (2*i+1), end="")
#     print(" " * (n-i-1))

# n=int(input("How many line do you want to print: "))
# for n in range(1,n+1):
#     for j in range(1,n+1):
#         if(j>=1 and j<=n):
#             print("* ",end=" ")
#         else:
#             print("  ",end=" ")
#     print("\n")

# n = 4
# for i in range(4):
    # print("*" * (i+1))

# n=int(input("How many line do you want to print: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==1 or i==n and j>=1 and j<=n):
#             print("* ",end=" ")
#         elif(j==1 or j==n):
#             print("* ",end=" ")
#         else:
#             print("  ",end=" ")
#     print("\n")

# n=3
# for i in range(3):
#     print("* "*(n))
#     print(" "*())
        
# n=int(input("Enter a number: "))
# for i in reversed(range(1,11)):
#     print(n,"*",i,"=",n*i)
    