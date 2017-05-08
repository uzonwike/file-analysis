import nltk
import string
import os, sys

from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import *

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

train_data = []
train_labels = []
test_data = []
test_labels = []
labels = ['pos', 'neg']

def annotate_files(dir_name):

    # Annotate the train and test data
    for label in labels:
        full_path = os.path.join(dir_name, label)
        file_count = 0
        total_files = len(os.listdir(full_path))

        for fname in os.listdir(full_path):
            file_count += 1
            with open(os.path.join(full_path, fname), 'r') as f:
                content = f.read()
                if file_count > (total_files / 3): # Using 1/3 of dataset for testing and remaining for training the model
                    test_data.append(content)
                    test_labels.append(label)
                else:
                    train_data.append(content)
                    train_labels.append(label)

# Breaks the strings into a list of individual tokens
def sentence_tokenizer(sentence):
    if len(sentence) == 0:
        raise Exception("The given sentence is empty")
    else:
        lower_sentence = sentence.lower()
        tokenized_sentences = lower_sentence.split('.')
        return tokenized_sentences

# Stem the tokens to reduce inflected words to their roots
def stem_tokens(tokens):
    stemmed = []
    stemmer = PorterStemmer()
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

# Remove uninformative words from a given sentence
def remove_stopwords(sentence):
    tokens = sentence_tokenizer(sentence)
    filtered = [w for w in tokens if not w in set(stopwords.words('english'))]
    return filtered

# Build vectors from features
def feature_to_vec(train_data):
    count_vectorizer = CountVectorizer()
    feature_train_data_counts = count_vectorizer.fit_transform(train_data)
    return feature_train_data_counts

# Transform the corpus into vectors matching the occurence of words relative to all the documents
def vectorize(train_data, test_data):
    vectorizer = TfidfVectorizer(min_df=5,
                                 max_df = 0.8,
                                 sublinear_tf=True,
                                 use_idf=True)
    train_vectors = vectorizer.fit_transform(train_data)
    test_vectors = vectorizer.transform(test_data)
    return (train_vectors, test_vectors)

def classifier(train_data, test_data):
    train_test_vectors = vectorize(train_data, test_data)
    clf = MultinomialNB()
    clf.fit(train_test_vectors[0], train_labels)
    print clf.predict(train_test_vectors[1])

annotate_files("./data/test/")
classifier(train_data, test_data)
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
