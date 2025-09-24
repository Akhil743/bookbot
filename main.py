import sys
from stats import count_words, count_characters, chars_dict_to_sorted_list


# python
# python
# python
def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def main():
    # Check for the correct number of command-line arguments.
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the book path from the command line instead of hard-coding it.
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = count_words(text)
    char_counts = count_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_counts)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print(f"--------- Character Count -------")

    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print(f"============= END ===============")


main()
