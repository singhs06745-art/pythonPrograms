from collections import Counter
import re
def word_frequency(sentence):
    words = re.findall(r"\b\w+\b", sentence.lower())
    return dict(Counter(words))
