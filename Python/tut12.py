a=2
def fun():
    global a
    a=3
    print(a)
fun()
print(a)
list1=[1,2,3,4,5,6,7,7,89,9,9.9]
list2=[item for item in list1 if item%2==0] #--> This is comprehension method you can change list after applying condtions or without condition.
print(list2)
s={i for i in list1} #--> You can also apply comprehension method for set and dictionary
print(s)
t=(i for i in list1) #--> You can not applly Comprehension method in tupple.
print(t)
# for i , item in enumerate(list1): #--> This is enumerate function you can access list item and index.
#     print(i,item)
while(True):
    print("Press q for quite")
    n=input("Enter a number: ")
    if n=='q':
        break
    try:
        n=int(n)
        c=1/n
        print(c)
    # except : #--> You dont want to use this error And is you use this error use very carefully because its impact on user experience
    #     raise ValueError("This is Value Error")
    except ZeroDivisionError as e:
        # print("Error showed") --> You can use this instead of finally but in terms of more than one error and more than one line of code finally is helpful
        print("-~-~-~-~-Any number cannt divide by zero its a rule-~-~-~-~-")
    except ValueError as e:
        print("~~~~~You entered something which is not Number~~~~~")
    except:
        print("Please Try again!!!")
    else: #--> When you want to print a message which indicates a program is suucessfully run
        print("Thanks for using Program. Hope you like it.")
    finally: #--> When you want to know some error showed you can use finally
        print("Error Showed.")