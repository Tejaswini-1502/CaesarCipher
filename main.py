import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
  text = list(text)
  n = len(text)
  for i in range(n):
    if text[i] in alphabet:
      j = alphabet.index(text[i])
      if direction=="encode":
        text[i] = alphabet[(j+shift)%26]
      else:
        if shift > j:
          text[i] = alphabet[j-shift+26]
        else:
          text[i] = alphabet[j-shift]
            
  if direction=="encode":
    print(f"Encrypted text: {''.join(text)}")
  else:
    print(f"Decrypted text: {''.join(text)}")  

print(art.logo)
done = "no"
while done == "no":
  direction_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text_input = input("Type your message:\n").lower()
  shift_input = int(input("Type the shift number:\n"))
  caesar(text = text_input, shift = shift_input, direction = direction_input)
  done = input("Type 'yes' if done. Otherwise type 'no' to continue.")

print("Goodbye xD")
