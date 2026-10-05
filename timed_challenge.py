# Question 5: Unique Word Count
# Count how many distinct words are in the collection.
# Input: "one fish two fish red fish blue fish"
# Output: 5

def unique_word_count(text):
    if not isinstance(text, str):
        return 0

    words = text.split()
    unique_words = set(words)

    return len(unique_words)


# Test cases
print(unique_word_count("one fish two fish red fish blue fish"))
print(unique_word_count(""))
print(unique_word_count("hello hello hello"))
print(unique_word_count("Python Java Python C++"))
