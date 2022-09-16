# with open("poem.txt",) as f:
#     data=f.read()
#     print(data)
#     data.casefold()
#     word="twinkle"
#     if word in data:
#         print ("success")


# def game():
#     userscore=int(input("Enter your score : "))
#     return userscore
# score= game()   
# with open('hiscore.txt', 'r') as f:
#     data = f.read(); 
# if data=='':
#     with open('hiscore.txt', 'w') as f:
#         f.write(str(score))
# elif int(data)<score:
#     with open('hiscore.txt', 'w') as f:
#         f.write(str(score))

# for i in range(2,21):
#     with open(f"table/multiplication_of_{i}.txt",'w') as f:
#         for j in range(1,11):
#             f.write(f"{i} X {j} = {i*j}")
#             if(j!=10):
#                 f.write("\n")

# with open("this.txt") as f:
#     data = f.read()
# data=data.replace("donkey","*****")
# with open("this.txt",'w') as f:
#     f.write(data)

# words=["donkey","billu","fuddu"]
# with open("this.txt") as f:
#     data = f.read()
# for word in words:
#     data=data.replace(word,"@#$%^&")
# with open("this.txt",'w') as f:
#     f.write(data)

# with open("log.txt") as f:
#     data=f.read()
# if "python" in data.lower():
#     print("Python is in file")
# else:
#     print({"Python is not in file"})

# data=True
# i=1
# with open("log.txt") as f:
#     while data:
#         data=f.readline()
#         if "python" in data.lower():
#             print(f"Python is in line no {i}")
#         i+=1

# with open("this.txt") as f:
#     data=f.read()
# with open("copy,txt","w") as f:
#     f.write(data)

# file1="log.txt"
# file2="this.txt"
# with open(file1) as f:
#     data1=f.read()
# with open(file2) as f:
#     data2=f.read()
# if data1==data2:
#     print("Files are identical")
# else:
#     print("Files are not identical")

# with open("copy.txt","w") as f:
#     f.write("")
import os
# file="copy.txt"
newfile="newcopy.txt"
# with open(file) as f:
#     data=f.read()
# with open(newfile,"w") as f:
#     f.write(data)
os.rename(newfile,"copy.txt")