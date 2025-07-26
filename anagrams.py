word1 = input("Enter first word: ").replace(" ", "").lower()
word2 = input("Enter second word: ").replace(" ", "").lower()

if sorted(word1) == sorted(word2):
    print("They are anagrams!")
else:
    print("They are not anagrams.")