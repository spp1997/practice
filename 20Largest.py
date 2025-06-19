numbers = [5, 3, 9, 7, 9]

# Remove duplicates to handle repeated max values
unique_numbers = list(set(numbers))

# Sort in descending order
unique_numbers.sort(reverse=True)

# Get the second largest
second_largest = unique_numbers[1]

print(second_largest)  # Output: 7