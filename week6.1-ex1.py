from typing import List, Set, Iterable
from time import time

WORDS_FILE_PATH = r"C:\Users\97252\python\Notebooks\week06\resources\words.txt"
word_to_search = "zwitterion"
times_to_search = 1000


def create_list_from_file() -> List:
    """
    The function opens the file and creates a list of the words that it contains.
    :return: The created list.
    """
    with open(WORDS_FILE_PATH, 'r') as words:
        words_list = [line for line in words]
    return words_list


def create_set_from_file() -> Set:
    """
    The function opens the file and creates a set of the words that it contains.
    :return: The created set.
    """
    with open(WORDS_FILE_PATH, 'r') as words:
        words_set = [line for line in words]
    return set(words_set)


def average_runtime(words: Iterable) -> float:
    """
    The function calculates the average time to search a word in the received list/set.
    :param words: The list or the set to search in.
    :return: The average time that it takes to search the current word.
    """
    total_time = 0.0
    for index in range(times_to_search):
        start_time = time()
        words.__contains__(word_to_search)
        end_time = time()
        total_time += (end_time - start_time)
    return total_time / times_to_search


if __name__ == '__main__':
    list_of_words = create_list_from_file()
    set_of_words = create_set_from_file()
    print(average_runtime(list_of_words))
    print(average_runtime(set_of_words))



