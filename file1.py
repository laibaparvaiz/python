import string 

filename = input("Enter a file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
    exit()

letter_counts = {letter: 0 for letter in string.ascii_lowercase}
for char in content:
    if char.isalpha():
        lower_char = char.lower()
        letter_counts[lower_char] += 1

sorted_counts = sorted(
    letter_counts.items(),
    key = lambda x: x[1],
    reverse = True
    )

for letter in sorted(letter_counts):
    count = letter_counts[letter]
    if count > 0:
        print(f"{letter} -> {count}")