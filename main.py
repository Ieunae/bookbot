def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"Found {num_words} total words")

def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import word_count

main()