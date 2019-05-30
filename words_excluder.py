"""
Simple tool for selecting words from list by their length.
"""

def exclude_by_length(self):
    """ Exclude words from list. Criteria is minimal length given by user."""
    longer_words = []

    user_input = int(input('Exclude words shorter than: '))

    for item in self:
        if len(item) >= user_input:
            longer_words.append(item)

    return(longer_words)
