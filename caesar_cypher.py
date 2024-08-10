def caesar_cipher(text, shift, mode):
  result = ""

  for char in text:

    # this encrypts and decrypts upper case characters in the range from A TO Z
    if char.isupper():
      if mode == 'encrypt':
        result += chr((ord(char) + shift - 65) % 26 + 65)
      elif mode == 'decrypt':
        result += chr((ord(char) - shift - 65) % 26 + 65)

    # This encrypt/decrypt lowercase characters from a to z
    elif char.islower():
      if mode == 'encrypt':
        result += chr((ord(char) + shift - 97) % 26 + 97)
      elif mode == 'decrypt':
        result += chr((ord(char) - shift - 97) % 26 + 97)

    # This Leave spaces and other characters intact
    else:
      result += char

  return result

while True:
  text = input("Enter text (or 'quit' to exit): ")
  if text.lower() == 'quit':
    break

  try:
    shift = int(input("Enter shift value[1-25]: "))
    mode = input("Enter mode (encrypt/decrypt): ").lower()

    result = caesar_cipher(text, shift, mode)
    print("Result:", result)

  except ValueError:
    print("Invalid shift value. Please enter an integer.")
