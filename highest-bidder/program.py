import os
from art import logo
print(logo)
end = True
def highest_bidder(highbid):
    for i in highbid:
        highest = 0
        bid_amount = highbid[i]
        if bid_amount > highest:
            highest = bid_amount
            winner = i
        print(f"The highest bidder is {i} with the bidding amount of ${highest}")
while end:
    name = input("What's your name:\n")
    amount = int(input("What's the amount you want to bid:\n$"))
    highbidder = {}
    highbidder[name]=amount
    next = input("Any othr bidder? Type 'yes' or 'no'\n")
    if next == "no":
        end = False
        highest_bidder(highbidder)
    elif next == "yes":
        os.system('cls')
    else:
        print("Invalid")
        end = False

     
