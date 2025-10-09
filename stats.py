def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    letters = list(text)
    char_count = dict()
    for letter in letters:
        character = letter.lower()
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    return char_count
