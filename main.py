def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_letters = letter_count(text)
    sorted_letters = letter_sort(num_letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in sorted_letters:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import word_count, letter_count, letter_sort

main()