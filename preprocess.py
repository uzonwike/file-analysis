import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import *
import string

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
tf_transformer = TfidfTransformer()

# Retrieve features from a given sentence
def extract_features(sentence):
    if len(sentence) == 0:
        raise Exception("The sentence passed in is empty")
    else:
        return vectorizer.get_feature_names(sentence)

# Transform features to vectors
def get_feature_vector(sentence):
    features = extract_features(sentence)
    feature_count = vectorizer.fit_transform(features)
    return feature_count

# Get the term-document frequencies
def term_frequency(sentence):
    feature_vector = get_feature_vector(sentence)
    feature_tf = tf_transformer.fit_transform(feature_vector)
    return feature_tf

# Train the classifier with the term frequencies and targets (i.e positive and negative). This assumes that we pass in the list of indices of the targets. eg. target_idx = [0, 1] ("negative" => 0, "positive" => 1)
def train_classifier(feature_tf, targets_idx):
    clf = MultinomialNB().fit(feature_tf, targets_idx)
    return clf

def predict_sentiment_value(sentence, classifier):
    new_feature_count = vectorizer.transform(sentence)
    feature_transform = tf_transformer.transform(new_feature_count)
    return classifier.predict(feature_transform)

# Returns the predicted sentiment from the target array (i.e targets_list = ["negative", "positive"])
def get_sentiment_type(predicted_value, targets_arr):
    return targets_arr[predicted_value];

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

# Get accuracy score of classifier
def get_accuracy_score(clf, features, labels):
    return clf.score(features, labels)

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
