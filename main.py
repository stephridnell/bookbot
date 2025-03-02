import sys

from stats import (format_print_dictionary, get_character_occurrences,
                   get_word_count, sort_dictionary)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path) 
    word_count = get_word_count(book_text)
    character_counts = sort_dictionary(get_character_occurrences(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    format_print_dictionary(character_counts)
    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path, "r") as f:
        return f.read()

main()