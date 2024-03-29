# here is the full code of caesar cipher project using functions and conditional loops
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']','/','|',';',':',',','.','/','<','>','!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']','/','|',';',':',',','.','/','<','>']
def ceaser(direction_ips,word_text,shift_amount):
    ceaser_cipher = ""
    if direction_ips == "decode":
        shift_amount*=-1
    for i in word_text:
        if i in alphabet:
            position = alphabet.index(i)
            total = position + shift_amount
            ceaser_cipher+=alphabet[total]
        else:
             ceaser_cipher+=i
    print(f"The {direction_ips} Text is {ceaser_cipher}")
should_end = True
while should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  ceaser(word_text=text,shift_amount=shift,direction_ips=direction)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = False
    print("Goodbye!")
