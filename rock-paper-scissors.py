import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock,paper,scissors]
your_score = 0
comp_score = 0
no_of_play = int(input("HOW MANY TIMES YOU WANT TO PLAY?\n"))
for i in range(no_of_play):
  user_choice = int(input("What do you want to choose?\nType 0 for rock\nType 1 for paper\nType 2 for scissors\n"))
  if user_choice >= 3 or user_choice < 0:
    print (f"YOU TYPE AN INVALID NUMBER. YOU LOSE!\n\tYOUR SCORE = {your_score}\n\tCOMPUTER SCORE = {comp_score}")
  else:
    print("YOUR CHOICE:")
    print(game[user_choice],"\n")
    computer_choice = random.randint(0,2)
    print("COMPUTER CHOICE:\n")
    print(game[computer_choice]) 
    if user_choice == 0 and computer_choice == 2:
      your_score +=1
      print(f"YOU WIN!\n\tYOUR SCORE = {your_score}\n\tCOMPUTER SCORE = {comp_score}")
    elif computer_choice == 0 and user_choice == 2:
      comp_score+=1
      print(f"YOU LOSE\n\tYOUR SCORE = {your_score}\n\tCOMPUTER SCORE = {comp_score}")
    elif computer_choice > user_choice:
      comp_score+=1
      print(f"YOU LOSE\n\tYOUR SCORE = {your_score}\n\tCOMPUTER SCORE = {comp_score}")
    elif user_choice > computer_choice:
      your_score+=1
      print(f"YOU WIN!\n\tYOUR SCORE = {your_score}\n\tCOMPUTER SCORE = {comp_score}")
    elif computer_choice == user_choice:
      print(f"IT'S A DRAW\n\tYOUR SCORE = {your_score}\n\tCOMPUTER SCORE = {comp_score}")
print(f"FINAL SCORE:\n\tYOUR SCORE = {your_score}\n\tCOMPUTER SCORE = {comp_score}")
if your_score > comp_score:
  print("CONGRATULATIONS YOU WON!")
elif your_score == comp_score:
  print(f"IT'S A DRAW:\n YOUR SCORE:{your_score}\nCOMPUTER SCORE:{comp_score}")
else:
  print("COMPUTER WON THE GAME")

