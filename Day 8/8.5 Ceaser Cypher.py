alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def ceaser(text,shift,direction):
    output = ""
    if direction == "encode":
        shift *=  1
    elif direction == "decode":
        shift *= -1
        
    for chr in text:
        index = alphabet.index(chr)
        new_index = (index + shift)%26
        output += alphabet[new_index]
    print(f"The {direction}d text is {output}")
    
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

ceaser(text,shift,direction)
