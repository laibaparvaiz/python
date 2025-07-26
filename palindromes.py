text = input("Enter a text: ")
cleaned = text.replace(" ","").lower()
if cleaned == cleaned[::-1]:
    print("Its a palindrome.")
else:
    print("Its not a palindrome.")