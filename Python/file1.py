def greet(n):
    print(f"Good Morning,{n}")
print(__name__)
if __name__=="__main__":
    n=input("Enter a name ")
    greet(n)
print(__name__)