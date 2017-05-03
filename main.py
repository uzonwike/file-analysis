from os import listdir
from os.path import isfile, join
import file_parser
from sentiment_classifier import *
import database

def analyze_files(directory):
	# Get all file paths, load the classifier
	paths = [f for f in listdir(directory) if isfile(join(directory, f))]
	classifier = FileClassifier()

	# Do analysis for all files in dir
	for path in paths:
		# File data is a tuple (name, contents)
		file_data = file_parser.load_file(path)
		if file_data:
			sentiment = classifier.classify_text(file_data[1])
			# Save sentiments results and file data to database