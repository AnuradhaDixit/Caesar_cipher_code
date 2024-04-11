from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(plain_text,cipher_shift,cipher_direction):
  cipher_text = ""  
  if cipher_shift > 25:
    cipher_shift = cipher_shift % 25
  
  if cipher_direction == "decode":
    cipher_shift *= -1
    
  for char in plain_text: 
    if char in alphabet :
      new_index = alphabet.index(char) + cipher_shift
      if new_index > 25:
        new_index = new_index - len(alphabet)
      elif new_index < 0:
        new_index = new_index + len(alphabet)
      cipher_text += alphabet[new_index] 
    else:
      cipher_text += char
  print(f"Here's the {cipher_direction}d result: {cipher_text}")

should_restart = True
while should_restart:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(plain_text = text, cipher_shift = shift, cipher_direction = direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_restart = False
    print("Goodbye")
  