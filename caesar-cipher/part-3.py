alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(direction_ips,word_text,shift_amount):
    ceaser_cipher = ""
    if direction_ips == 'decode':
        shift_amount*=-1
    for i in word_text:
        position = alphabet.index(i)
        total = position + shift_amount
        ceaser_cipher+=alphabet[total]
    print(f"The {direction_ips} Text is {ceaser_cipher}")
ceaser(direction_ips=direction,word_text=text,shift_amount=shift)
        