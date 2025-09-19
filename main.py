import sys
from stats import get_word_count, get_letter_count, sort_by_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main(*args, **kwargs):
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    content = get_book_text(sys.argv[1])

    word_count = get_word_count(content)
    letter_count = get_letter_count(content)
    sorted = sort_by_count(letter_count)
    
    # Begin report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

main()