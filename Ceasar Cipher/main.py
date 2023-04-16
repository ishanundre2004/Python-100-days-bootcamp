import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue=True
def encode(text, shift):
    encoded_msg=""
    for char in text:
        for i in range(1,27):
            if alphabet[i]==char:
                encoded_msg+=alphabet[i+shift]
    print(encoded_msg)

def decode(text, shift):
    decoded_msg=""
    for char in text:
        for i in range(26,52):
            if alphabet[i]==char:
                decoded_msg+=alphabet[i-shift]
    print(decoded_msg)

while should_continue==True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction=="encode":
        encode(text, shift)
    elif direction=="decode":
        decode(text, shift)
    ask=input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if ask=="yes":
        should_continue=True
    elif ask=="no":
        should_continue=False
        print("Good Bye!")
    else:
        print("Invalid input.")
        ask=input("Type 'yes' if you want to go again. Otherwise type 'no'.")



    
    

