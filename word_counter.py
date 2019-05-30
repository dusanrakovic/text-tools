"""
Simple tool for counting frequency of words in some list. Suitable for list of tokenized words.
"""

from collections import Counter

def counting(self):
    """ Counting word from list. """
    counted_words = Counter(self)
    return(counted_words)
