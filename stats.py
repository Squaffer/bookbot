def word_count(text_input):
    words = text_input.split()
    return len(words)

def count_characters_in_file(text):
    char_counts = {}
    lower_text_only = text.lower()
    for line in lower_text_only:
        for char in line:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def sort_on(items):
    return items["num"]





