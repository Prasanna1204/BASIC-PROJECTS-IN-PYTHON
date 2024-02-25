import random
from art import logo
print(logo)
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user = []
computer = []
for i in range(0,2):
    user_cards = random.choice(cards)
    computer_cards = random.choice(cards)
    computer.append(computer_cards)
    user.append(user_cards)
def display():
    print(f"Your final cards : {user}")
    print(f"Computer's card : {computer}")
def condition():
    if 11 in user and sum(user)>21:
        user.remove(11)
        user.append(1)
        print(user)
        print(sum(user))
print(f"Your cards : {user}")
print(f"Computer's first card : {computer[0]}")
if sum(user)==21:
    display()
    print("Black Jack. You Win")
elif sum(computer)==21:
    print("Black Jack. Computer wins")
condition()
def computer_cond():
    while sum(computer)<17:
        computer_cards = random.choice(cards)
        computer.append(computer_cards)
    if sum(computer)>21:
            display()
            print("Computer Exceeds 21. You Win!")
    elif sum(computer)==21:
        display()
        print("Black Jack. Computer Wins")
    elif sum(user)==21:
        display()
        print("Black Jack. You Win")
    elif sum(user)>21:
        display()
        print("You Exceeds 21. Computer Wins")
    else:
        if sum(computer)<21 and (sum(user)>sum(computer)):
            display()
            print("You Win!")
        elif sum(user)<sum(computer):
            display()
            print("Computer win!")
        elif sum(user)==sum(computer):
            display()
            print("It's a draw")
while sum(user)<21:
    next_card = input("type 'y' for hit or 'n' for stand\n")
    if next_card == 'y':
        user_cards = random.choice(cards)
        user.append(user_cards)
        print(user)
        condition()
        computer_cond()
    elif next_card == 'n':
        computer_cond()
  




