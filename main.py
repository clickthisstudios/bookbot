def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document.")
    get_num_chars(text)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    letters = {}
    letter_list = []
    lower_case = text.lower()
    for c in lower_case:
        if c.isalpha():
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
    # print(letters)
    for char, num in letters.items():
        char_dict = {"char": char, "num": num}
        letter_list.append(char_dict)

    def sort_on(dict):
        return dict["num"]

    letter_list.sort(reverse=True, key=sort_on)
    for item in letter_list:
        print(f"The '{item['char']}' character appears {item['num']} times.")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()