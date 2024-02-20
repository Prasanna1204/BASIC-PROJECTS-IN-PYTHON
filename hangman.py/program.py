import random
from words import lists
from ascii_art import logo,stages
print(logo)
lives=6
display = []
var  = random.choice(lists)
Random = var.lower()
lenght = len(Random)
for i in range(0,lenght):
    display+='_'
find = True
while find:
    user_choice = input("Guess the letter: ").lower()
    for i in range(0,lenght):
       if Random[i]==user_choice:
           display[i]=user_choice
    print(f"YOU CHOOSE A CORRECT WORD: {user_choice}")
    print(f"{' '.join(display)}\n")
    if user_choice not in Random:
        lives-=1
        print(f"IT IS A WRONG WORD: {user_choice}")
        print(stages[lives])
        if lives==0:
            find = False
            print(f"YOU LOSE!\nTHE CORRECT WORD IS {Random}")
    if '_' not in display:
        find = False
        print("YOU WIN!!")