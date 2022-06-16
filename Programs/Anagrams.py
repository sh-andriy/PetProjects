def insert_symbol(string, index, symbol):
    return f"{string[:index]}{symbol}{string[index:]}"


def reverse_words(string):

    word_list = string.split()
    final_word = []

    for word in word_list:
        if not word.isalpha():

            symbols_array = []
            modified_word = ""

            for symbol_index in range(len(word)):
                letter = word[symbol_index]
                if not letter.isalpha():
                    symbols_array.append([letter, symbol_index])
                else:
                    modified_word += letter

            modified_word = modified_word[::-1]

            for symbol, index in symbols_array:
                modified_word = insert_symbol(modified_word, index, symbol)

            final_word.append(modified_word)
        else:
            final_word.append(word[::-1])

    return ' '.join(final_word)


if __name__ == "__main__":
    cases = [
        ("absd jkl", "dsba lkj"),
        ("a1bsd jk!l", "d1sba lk!j"),
        ("", "")
    ]

    for text, reverse_text in cases:
        print("{} -> {}".format(text, reverse_words(text)))
        assert reverse_words(text) == reverse_text
