from stats import num_of_words, characterCount, sortCharacters
import sys

def get_book_text(input):
    with open(input) as f:
        file_contents = f.read()
        return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    # print(book)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")
    print(f"Found {num_of_words(book)} total words")
    print("--------- Character Count -------")
    characters = characterCount(book)
    sortedCount = sortCharacters(characters)
    for k, v in sortedCount:
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")
main()