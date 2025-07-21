def mysplit(string):
    words = []
    word = ""

    for char in string:
        if char != " ":
            word += char
        else:
            if word != "":
                words.append(word)
                word = ""
    
    if word != "":  # Add the last word (if any)
        words.append(word)
        
    return words
    

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
    