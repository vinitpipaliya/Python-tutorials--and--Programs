import random

def gamewin(comp,user):
    if comp==user:
        return None
    elif comp=='s':
        if user=='w':
            return False
        elif user=='g':
            return True
    elif comp=='w':
        if user=='g':
            return False
        elif user=='s':
            return True
    elif comp=='g':
        if user=='s':
            return False
        elif user=='w':
            return True

randno=random.randint(1,3)
if randno==1:
    comp ='s'
elif randno==2:
    comp ='w'
else:
    comp ='g'
user=input("Enter s ,w or g: ")
win=gamewin(comp,user)
print("Computer choose: ",comp)
if(win==None):
    print("Tie")
elif win:
    print ("You win")
else:
    print("You lose")
