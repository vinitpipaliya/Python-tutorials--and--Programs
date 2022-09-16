from typing import List
par=input("Enter a parantheses I will tell you its valid or not: ")
a='(){}[]'
if (par=="()" or par=="{}" or par=="[]"): 
    print("Parantheses is valid")
elif par in a:
   print("Parantheses is valid")
else:
    print("Parantheses is not valid")
