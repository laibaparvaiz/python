word = input("Enter a word: ")
characters = input("Enter characters: ")
pos = -1
for char in word:
    pos = characters.find(char, pos + 1)
    if pos == -1:
        print("No.")
        break
else:
        print("Yes.")