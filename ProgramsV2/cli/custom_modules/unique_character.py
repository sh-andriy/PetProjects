from functools import lru_cache


@lru_cache(maxsize=1000)
def unique_character_calculator(data):
    if isinstance(data, str):

        char_dataset = {}
        unique_char = 0

        for character in data:
            if character not in char_dataset:
                char_dataset.update({character: 1})
            else:
                char_dataset[character] += 1

        for character in char_dataset:
            if char_dataset[character] == 1:
                unique_char += 1

        return unique_char

    else:
        raise ValueError("Input must be string!")
