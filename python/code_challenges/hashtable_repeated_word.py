from python.data_structures.hashtable import Hashtable
import string


def first_repeated_word(input):
    words = [word.strip(string.punctuation).lower() for word in input.split()]
    dict = Hashtable()
    for word in words:
        if dict.has(word):
            return word
        dict.set(word, None)
