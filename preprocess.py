import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import *
import string

from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('punkt')
nltk.download('stopwords')

# Breaks the strings into a list of individual tokens
def sentence_tokenizer(sentence):
    if len(sentence) == 0:
        raise Exception("The given sentence is empty")
    else:
        lower_sentence = sentence.lower()
        remove_punctuations = lower_sentence.translate(None, string.punctuation)
        tokens = word_tokenize(remove_punctuations)
        tokens_dict
        return tokens

# Creates a word frequency map
def word_frequency(words):
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

# Remove uninformative words from a given sentence
def remove_stopwords(sentence):
    tokens = sentence_tokenizer(sentence)
    filtered = [w for w in tokens if not w in set(stopwords.words('english'))]
    return filtered

# Stem the tokens to reduce inflected words to their roots
def stem_tokens(tokens):
    stemmed = []
    stemmer = PorterStemmer()
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed
