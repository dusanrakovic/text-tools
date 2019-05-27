"""
Simple tool for removing punctuations from string.
It removes following marks: ,.;:'"?!()[]{}
"""

import re

def remove_punct(self):
	"""Remove standard punctuation marks from given string"""
    text_without_punctuation = re.sub('[,\.\'\"\?\(\)!:;\[\]\{\}]', '', self)
    return(text_without_punctuation)
