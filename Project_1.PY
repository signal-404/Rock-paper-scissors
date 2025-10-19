'''
1 for rock
-1 for paper
0 for scissor

'''
import random

computer=random.choice([1,-1,0])
player=input("Enter your choice: ")
youdict={"r":1,"p":-1,"s":0}
reversedict={1:"rock",-1:"paper",0:"scissor"}
youchoice=youdict[player]

print(f"You chose {reversedict[youchoice]}\nComputer chose {reversedict[computer]}")

if(computer==youchoice):
    print("Its a draw")

else:
    if(computer ==-1 and youchoice ==1):
        print("you lose!")
    elif(computer ==-1 and youchoice ==0):
        print("you win!")
    elif(computer ==0 and youchoice ==-1):
        print("you lose!")
    elif(computer ==0 and youchoice ==1):
        print("you win!")
    elif(computer ==1 and youchoice ==0):
        print("you lose!")
    elif(computer ==1 and youchoice ==-1):
        print("you lose!")
    else:
        print("Something went wrong!")
