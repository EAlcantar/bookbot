from stats import number_of_words
from stats import character_count
from stats import sort_characters_by_count
import sys

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        # f is a file object
        return f.read()
    
def print_character_report(sorted_characters):
    for item in sorted_characters:
        if item['character'].isalpha():  # Skip non-alphabetical characters
            print(f"{item['character']}: {item['count']}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1] #"books/frankenstein.txt"
    book_text = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    number_of_words(book_text)
    print("--------- Character Count -------")
    print_character_report(sort_characters_by_count(character_count(book_text)))
    print("============= END ===============")

main()