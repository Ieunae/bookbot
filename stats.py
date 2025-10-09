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

def letter_sort(char_count):
    def sort_on(char_count):
        return char_count["num"]
    
    char_list = []
    for key, value in char_count.items():
        char_dict = {"char": key, "num": value}
        char_list.append(char_dict)  # No return here!
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list
