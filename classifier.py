from nltk import word_tokenize
from nltk.corpus import stopwords

# Breaks the strings into a list of individual tokens
def sentence_tokenizer(data):
    if len(data) == 0:
        raise Exception("The given tuple is empty")
    else:
        sentence = data[1]
        tokens = word_tokenize(data[1])
        return tokens

def bag_of_words(words):
    if len(words) == 0:
        raise Exception("The string is empty")
    else:
        map = {}
        for str in words:
            if (str not in map):
                map[str] = 1
            else:
                map[str] = map.get(str) + 1
        return map
