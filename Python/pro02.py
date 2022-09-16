import random
randNumber=random.randint(1,100)
print("----------------")
print("Lets play a Game")
print("I am picking a number berween 1 to 100")
print("You have to guesss which number I guessed")
print("----------------")
guess=0
user=None
while(randNumber!=user):
    user=int(input("Enter a number: "))
    print("----------------")
    guess+=1
    if user==randNumber:
        print("****You guessed Correct Number!****")
    else:
        if user>randNumber:
            print("You guessed wrong number. Enter smaller number")
        else:
            print("You guessed wrong number. Enter larger number")
print(f"You guess correct number in '\033[1m{guess}\033[0m' guess.")
with open("hiscore.txt")as f:
    hiscore=int(f.read())
if guess<hiscore:
    print("Congratulation!! You created Highscore.")
    with open("hiscore.txt","w") as f:
        f.write(str(guess))
