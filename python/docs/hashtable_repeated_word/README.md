# Challenge Summary

* Write a function called “first_repeated_word” that removes punctuation and finds the first word to occur more than once in a string.

## Whiteboard Process
- Will update later
![]()

## Approach & Efficiency

Approach
*
- first i have to separate each word into a string and remove convert it to lowercase
- Probably create a hash table
- go through every word in the list and if that word already exist in the hash table  then return that word
- if not then just add that word to the hash table

Efficiency
* Time: O(n^2) - must iterate through list of words and then use “has” method to search for word in the Hash Table.
* Space: O(n) - linear space due to the list of words that needs to be created.

## Solution

The solution code is located in the `code_challenges/hashtable_repeated_word.py` file.

1. Within the virtual environment, install pytest via `pip install pytest`.
2. From the Python folder, run tests via `pytest tests/code_challenges/test_hashtable_repeated_word.py`.

## Contributors
- Angelos
- Aubrey
