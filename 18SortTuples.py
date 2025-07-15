students = [("Alice", 88), ("Bob", 75), ("Charlie", 93)]

# Sort by the second element (score) in ascending order
sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)
# Output: [('Bob', 75), ('Alice', 88), ('Charlie', 93)]
