list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

# Keep elements in the order they appear in list1
common = [x for x in list1 if x in list2]

print(common)  # Output: [3, 4]
