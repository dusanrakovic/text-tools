"""
Tool for tokenizing text into words. Requires nltk package installed.
"""

from nltk.tokenize import TreebankWordTokenizer

def tokenizing(self):
    """ Tokenize text source into words. """
    tokenizer = TreebankWordTokenizer()
    words = tokenizer.tokenize(self.lower())
    return words
