input = ("Th1s 1s a t3st str1ng w1th numb3rs 12345.")  # Example input string
result = ""   # Initialize an empty string to store the result
for ch in input :    # Iterate through each character in the input string
    if not ch.isdigit():    # Check if the character is not a digit
        result += ch        # If not a digit, append it to the result string
print(result)               # Print the final result string without digits
