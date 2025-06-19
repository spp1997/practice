def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:      # first time we see this element
            seen.add(item)        # mark it as seen
            result.append(item)   # keep it in the output list
    return result


# Example usage
numbers = [1, 2, 2, 3, 4, 3]
unique_numbers = remove_duplicates_preserve_order(numbers)
print(unique_numbers)  # Output: [1, 2, 3, 4]