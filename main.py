from stats import count_words, count_chars, sort_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents





def main():
    print("============ BOOKBOT ============")
    try:
        print(sys.argv[1])
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
    text = get_book_text(sys.argv[1])
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    chars = count_chars(text)
    sorted = sort_list(chars)
    #print(sorted)
    for item in sorted:
        print(f"{item['char']}: {item['num']}")  

    print("============= END ===============")


main()

