import random
print("Welcome to number guessing game")
print("I'm thinking a number between 1 to 100")
com_no = random.randint(1,100)
def level_easy(computer_no):
    for i in range(1,11):
        print(f"You have {11-i} attempts remaining to guess the number")
        guess = int(input("Guess a number:\n"))
        if guess>computer_no:
            print("Too High")
        elif guess < computer_no:
            print("Too low")
        else:
            print(f"You go it. The answer is {computer_no}")
            break
def level_hard(computer_no):
    for i in range(1,6):
        print(f"You have {6-i} attempts remaining to guess the number")
        guess = int(input("Guess a number:\n"))
        if guess>computer_no:
            print("Too High")
        elif guess < computer_no:
            print("Too low")
        else:
            print(f"You go it. The answer is {computer_no}")
            break
level = input("Choose a difficulty. Type 'Hard' or 'easy': ")
if level == 'Easy':
    level_easy(com_no)
elif level == 'hard':
    level_hard(com_no)
