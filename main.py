def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_characters(text)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    char_count = {}

    for char in text:
        lowercase_char = char.lower()
        if lowercase_char.isalpha():
            if lowercase_char not in char_count:
                char_count[lowercase_char] = 1
            else:
                char_count[lowercase_char] += 1

    return char_count

main()