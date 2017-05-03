from os import listdir
from os.path import isfile, join
import file_parser
from sentiment_classifer import *
import database

def load_files(directory):
	paths = [f for f in listdir(directory) if isfile(join(directory, f))]
	classifier = FileClassifer()

	# Do analysis for all files in dir
	for path in paths:
		# File data is a tuple (name, contents)
		file_data = load_file(path)
		if file_data:
			sentiment = classifier.classify_text(file_data[1])
			print(sentiment)
			# Save sentiments results and file data 

