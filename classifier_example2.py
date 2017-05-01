import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
 
# Special formatting for feature
def word_to_feature(word):
    return {word: True}

# Extract word from feature
def feature_to_words(feature):
  return feature[0].keys()

# Extract all words as features with a given sentiment from a file
def get_features_from_file(file_name, sentiment):
  features = []
  with open(file_name, 'r') as file:
    for line in file:
      word = line.strip()
      if len(word) >= 3 and len(word) < 12:
        features.append((word_to_feature(word), sentiment))
  return features

# Generate features from text for classifying
def generate_features(text, model_features):
  text_words = set(text)
  text_features = {}
  for feature in model_features:
      words = feature_to_words(feature)
      for word in words:
        text_features['contains('+word+')'] = (word in text_words)
  return text_features

# Create and train the classifier based on the postive and negative words
pos_features = get_features_from_file('./data/positive-words.txt', 'positive')
neg_features = get_features_from_file('./data/negative-words.txt', 'negative')
model_features = pos_features + neg_features
classifier = NaiveBayesClassifier.train(model_features)

# Input document to see the result
text = ''
document_features = generate_features(text.split(), model_features)
print(classifier.classify(document_features))