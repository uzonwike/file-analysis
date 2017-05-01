import nltk

# This is where we will to store our training words
file_words = []

# The sentiment analysis
# Created by following:
# http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/

# This just returns a list of all words without the sentiments
def get_words(words):
    all_words = []
    for (words, sentiment) in words:
      all_words.extend(words)
    return all_words

# This just returns an ordering of the words
# Probably not needed since each word occurs once?
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

# Some weird setup for extracting features
# NOTE: This uses the global file_words list
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in get_word_features(get_words(file_words)):
        features['contains(%s)' % word] = (word in document_words)
    return features

# Create the classifier
def create_classifier():
  # Files containing positive and negative words
  good = open('./data/positive-words.txt', 'r')
  bad = open('./data/negative-words.txt', 'r')

  # Read from our source files and seed words as negative/positive
  for line in good:
    if(len(line) >= 3 and len(line) < 15):
      file_words.append(([line.strip()], 'positive'))

  for line in bad:
    if(len(line) >= 3 and len(line) < 15):
      file_words.append(([line.strip()], 'negative'))

  # Close files
  good.close()
  bad.close()

  # Create classifier
  training_set = nltk.classify.apply_features(extract_features, file_words)
  classifier = nltk.NaiveBayesClassifier.train(training_set)
  return classifier

# Here is what we can do to analyze text
classifier = create_classifier()
text = 'hello darkness I am down and upset'
print(classifier.classify(extract_features(text.split())))