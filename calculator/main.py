from art import logo
import os
def add(one,two):
    return one+two
def sub(one,two):
    return one-two
def mul(one,two):
    return one*two
def div(one,two):
    return one/two
def calculator():
    print(logo)
    number_1 = int(input("What's the first number? "))
    should_continue = True
    while should_continue:
        symbol   = input("\n+\n-\n*\n/\nPick an operation: ")
        number_2 = int(input("What's the next number? "))
        if symbol == '+':
            output = add(number_1,number_2)
            print(f"{number_1} + {number_2} = {output}")
        elif symbol == '-':
            output = sub(number_1,number_2)
            print(f"{number_1} - {number_2} = {output}")
        elif symbol == '*':
            output = mul(number_1,number_2)
            print(f"{number_1} * {number_2} = {output}")
        elif symbol == '/':
           output = round(div(number_1,number_2),2)
           print(f"{number_1} / {number_2} = {output}")
        cont = input(f"Type 'yes' to continue calculating with {output}, or type 'no' for new calcultion ")
        if cont == 'yes':
           number_1 = output
        elif cont == 'no':
          should_continue = False
          os.system('cls')
          calculator()
calculator()
 

