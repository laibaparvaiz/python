value = input("enter an encrpt: ")
while True:
    try: 
       shift = int(input("Enter a text from (1 to 25): "))
       if 1 <= shift <= 25:
          break
       else:
          print('Shift must be between 1 to 25: ')
    except ValueError:
       print("shift is invalid: ")

cipher = ''
for char in value:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        cipher += chr((ord(char) - base + shift) % 26 + base)
    else:
        cipher += char

print("Encrypted text:", cipher)