print("--------------------------")
cab1=int(input("Enter the charges of first cab : "))
cab2=int(input("Enter the charges of second cab : "))
print("--------------------------")
if cab1>cab2:
    print("Choose second cab")
elif cab1<cab2:
    print("Choose first cab")
else:
    print("Choose any of them")