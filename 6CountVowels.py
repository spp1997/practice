def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count


text = input("Enter a string: ")
vowel_count = count_vowels(text)
print("Number of vowels:", vowel_count)
