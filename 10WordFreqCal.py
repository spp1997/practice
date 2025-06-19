# Word Frequency Counter

# Read a sentence from the user (remove leading/trailing spaces)
sentence = input("Enter a sentence: ").strip()

# Convert to lowercase and split on whitespace
words = sentence.lower().split()

# Build the frequency dictionary
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

# Print results
for word, count in freq.items():
    print(f"{word}: {count}")