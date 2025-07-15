# Example list with duplicates
items = [2, 5, 2, 7, 5, 9, 7]

# Create an ordered list of unique elements
unique_items = list(dict.fromkeys(items))

print("Unique values:", unique_items)
