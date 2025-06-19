text = "racecar"
reversed_text = ""

# Manually reverse the string
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

# Check if original and reversed strings are the same
if text == reversed_text:
    print(True)
else:
    print(False)



#text = "racecar"

#is_palindrome = text == text[::-1]  # Reverse the string and compare

#print(is_palindrome)  # Output: True