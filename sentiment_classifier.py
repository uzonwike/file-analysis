import nltk.classify.util
from nltk.classify import NaiveBayesClassifier

# Special formatting for feature
def word_to_feature(word):
    return {word: True}

# Get words from list of features
def get_words(words):
    all_words = []
    for (words, sentiment) in words:
      all_words.extend(words)
    return all_words

# Extract all words as features with a given sentiment from a file
def get_features_from_file(file_name, sentiment):
  features = []
  with open(file_name, 'r') as file:
    for line in file:
      word = line.strip()
      if len(word) >= 3 and len(word) < 12:
        features.append((word_to_feature(word), sentiment))
  return features

# Create and train the classifier based on the postive and negative words
pos_features = get_features_from_file('./data/positive-words.txt', 'positive')
neg_features = get_features_from_file('./data/negative-words.txt', 'negative')
model_features = pos_features + neg_features

# Generate features from text for classifying
# Credit to http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/
def generate_features(text):
  text_words = set(text)
  text_features = {}
  for word in get_words(model_features):
    text_features['contains('+word+')'] = (word in text_words)
  return text_features

training_set = nltk.classify.util.apply_features(generate_features, model_features)
classifier = NaiveBayesClassifier.train(training_set)

# Input document to see the result
text = 'I am an amazing person who loves to eat cake'
print(classifier.classify(generate_features(text.split())))
