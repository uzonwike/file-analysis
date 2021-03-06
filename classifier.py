import string
import os, sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# A class to handles classification and prediction 
# Parts of classifier were created with the help of:
# https://marcobonzanini.com/2015/01/19/sentiment-analysis-with-python-and-scikit-learn/

class FileClassifier:
    def __init__(self, train_dir):
        self.train_data = []
        self.train_labels = []
        # Sentiment labels
        self.labels = ['pos', 'neg']
        # Create TfidVectorizer
        self.vectorizer = TfidfVectorizer(min_df=5,
                                     max_df = 0.8,
                                     sublinear_tf=True,
                                     use_idf=True,
                                     decode_error='ignore')
        # Annotate the files from the training set
        self.annotate_files(train_dir)

    # Annotate the data
    def annotate_files(self, dir_name):
        # Iterate over labels/words and annotate them
        for label in self.labels:
            count = 0
            # Look in the folders for the corresponding labels
            full_path = os.path.join(dir_name, label)

            # Read the file
            for fname in os.listdir(full_path):
                with open(os.path.join(full_path, fname), 'r') as f:
                    content = f.read()
                    self.train_data.append(content)
                    self.train_labels.append(label)
                    count += 1
            print("Annotated " + str(count) + " files as '" + label + "'.")

    # Transform the corpus into vectors matching the occurence of words relative to all the documents
    def vectorize(self, document):
        # Classify the document based on train_data
        train_vectors = self.vectorizer.fit_transform(self.train_data)
        test_vectors = self.vectorizer.transform(document)
        return (train_vectors, test_vectors)

    # Classify text data
    def classify(self, document):
        train_test_vectors = self.vectorize(document)
        clf = MultinomialNB()
        clf.fit(train_test_vectors[0], self.train_labels)
        return clf.predict(train_test_vectors[1])
