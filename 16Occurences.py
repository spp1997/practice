numbers = [1, 2, 3, 2, 4, 2]
value = 2

# Method 1: Using the built‑in list.count()
occurrences = numbers.count(value)
print(occurrences)           # Output: 3

# ---- OR, if you prefer doing it manually ----
count = 0
for item in numbers:
    if item == value:
        count += 1
print(count)                 # Output: 3