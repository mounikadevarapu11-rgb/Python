import re
word = input("Enter word: ")
edited_word = re.sub(r'[^A-Za-z0-9]+', '', word)
print( edited_word)