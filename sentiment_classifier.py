import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
 
class FileClassifier:
  def __init__(self):
  # Create and train the classifier based on the postive and negative words
    pos_features = self.get_features_from_file('./data/positive-words.txt', 'positive')
    neg_features = self.get_features_from_file('./data/negative-words.txt', 'negative')
    self.model_features = pos_features + neg_features

    training_set = nltk.classify.util.apply_features(self.generate_features, self.model_features)
    self.classifier = NaiveBayesClassifier.train(training_set)

  # Special formatting for feature
  def word_to_feature(self, word):
      return {word: True}

  # Get words from list of features
  def get_words(self, words):
      all_words = []
      for (words, sentiment) in words:
        all_words.extend(words)
      return all_words

  # Extract all words as features with a given sentiment from a file
  def get_features_from_file(self, file_name, sentiment):
    features = []
    with open(file_name, 'r') as file:
      for line in file:
        word = line.strip()
        if len(word) >= 3 and len(word) < 12:
          features.append((self.word_to_feature(word), sentiment))
    return features

  # Generate features from text for classifying
  # Credit to http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/
  def generate_features(self, text):
    text_words = set(text)
    text_features = {}
    for word in self.get_words(self.model_features):
      text_features['contains('+word+')'] = (word in text_words)
    return text_features

  # Classify text
  def classify_text(self, text):
    return self.classifier.classify(self.generate_features(text.split()))