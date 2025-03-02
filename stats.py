def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_character_occurrences(book_text):
    character_occurrences = {}

    for character in book_text:
        character = character.lower()
        if character in character_occurrences:
            character_occurrences[character] += 1
        else:
            character_occurrences[character] = 1

    return character_occurrences

def sort_dictionary(dictionary):
    sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_dictionary

def format_print_dictionary(dictionary):
    for key, value in dictionary:
        if key.isalpha():
          print(f"{key}: {value}")