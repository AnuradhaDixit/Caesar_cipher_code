alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = str(input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")).lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
  cipher_list = []
  text_list = list(text)  
  for letter in text:
    new_index = alphabet.index(letter) + shift
    if new_index > 25:
      new_index = new_index-len(alphabet)
    cipher_list += alphabet[new_index] 
  #print(cipher_list)
  cipher_text = "".join(cipher_list)
  print(cipher_text)

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
  cipher_list = []
  #text_list = list(text)  
  for letter in text:
    new_index = alphabet.index(letter) - shift
    if new_index < 0:
      new_index = new_index + len(alphabet)
    cipher_list += alphabet[new_index] 
  #print(cipher_list)
  cipher_text = "".join(cipher_list)
  print(cipher_text)
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message. 
if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)
else:
  print("Wrong Input")