print('Welcome to the tip calculator! ')
amount = float(input('What was the total bill? $'))
tips = int(input('what percentage tip would you like to give? 10,12 or 15? '))
split = int(input('How many people to split the bill? '))
tips_plus_amount = ((tips/100) * amount)+amount
total = tips_plus_amount/split
total_amount = round(total,2)
print(f'Each person should pay ${total_amount}')

                     
                     
