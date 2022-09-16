# try:
#     f=open("1.text")
#     f=open("2.text")
#     f=open("3.text")
# except Exception as e:
#     print("File is not found.")

# list1=[1,2,3,4,5,6,7,8,9]
# for i ,item in enumerate(list1):
#     i+=1
#     if i==3 or i==5 or i==7:
#         print(i,item)

# n=int(input("Enter a number: "))
# list1=[n*i for i in range(1,11)]
# print(list1)

# print("You want a/b division?")
# while(True):
#     print("Press 'q' to quite")
#     a=input("Enter a number: ")
#     if a=='q' :
#         print("Thanks for visiting")
#         break
#     b=input("Enter b number: ")
#     if b=='q' :
#         print("Thanks for visiting")
#         break
#     try:
#         a=int(a)
#         b=int(b)
#         n=a/b
#         print(n)
#     except ZeroDivisionError as e:
#         print("Infinite value.")
#     except:
#         print("Invalid Input.")
   
# n=int(input("Enter a number: "))
# list1=[n*i for i in range(1,11)]
# print(list1) 
# with open("table.txt","a") as f:
#     f.write(str(list1))
#     f.write("\n")