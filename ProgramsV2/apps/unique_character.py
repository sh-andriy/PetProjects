from functools import lru_cache
import collections


@lru_cache(maxsize=1000)
def unique_character_calculator_dict(data):
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


@lru_cache(maxsize=1000)
def unique_character_calculator_list_comp(data):
    if isinstance(data, str):
        return sum([i for s, i in collections.Counter(data).items() if i == 1])
    else:
        raise ValueError("Input must be string!")


@lru_cache(maxsize=1000)
def unique_character_calculator_collections(data):
    if isinstance(data, str):
        symbols_dataset = collections.Counter(data).most_common()
        unique_counter = 0
        for symbol, amount in symbols_dataset:
            if amount == 1:
                unique_counter += 1
        return unique_counter
    else:
        raise ValueError("Input must be string!")
