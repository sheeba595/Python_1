# ----------------------------------
# Unique Word Counter from Paragraph
# ----------------------------------

# 1. Get paragraph from user
paragraph = input("Enter a paragraph:\n")

# 2. Convert paragraph to lowercase and split into words
words = paragraph.lower().split()

# Convert list to set to get unique words
unique_words = set(words)

# 3. Frozen set of common words
common_words = frozenset({"is", "a", "the", "and", "to", "of", "in"})

# 4. Remove common words using difference()
filtered_words = unique_words.difference(common_words)

# 5. Display results
print("\nUnique Words (after removing common words):")
for word in filtered_words:
    print(word)

print("\nTotal Unique Words:", len(filtered_words))
