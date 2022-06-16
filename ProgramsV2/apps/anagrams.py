def insert_symbol(string, index, symbol):
    return f"{string[:index]}{symbol}{string[index:]}"


def reverse_words(string):

    if type(string) == str:
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
    else:
        raise ValueError('Text must be string')

    return ' '.join(final_word)
