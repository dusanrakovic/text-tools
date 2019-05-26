"""
Simple tool for cleaning HTML tags and newlines from string.

"""

import re

def clean_tags(self):
"""Remove opening and closing HTML tags and cleaning newlines."""
    del_front_tags = re.sub('<\s*\w.*?>', '', self)
    del_back_tags = re.sub('<\s*\/\s*\w\s*.*?>|<\s*br\s*>', '', del_front_tags)
    stripped = del_back_tags.rstrip()
    cleaned_text = re.sub('\n', ' ', stripped)
    return(cleaned_text)
