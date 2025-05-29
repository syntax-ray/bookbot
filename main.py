from stats import count_words, count_characters, sort_charcter_count

def get_book_text(path):
    content = None
    with open(path) as file:
        content = file.read()
    return content


def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    character_counts = count_characters(text)
    sorted_character_counts = sort_charcter_count(character_counts)
    # print(sort_charcter_count(character_counts))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k, v in sorted_character_counts.items():
        print(f"{k}: {v}")




main()