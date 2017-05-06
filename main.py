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
	database.db.connect()
	for path in paths:
		# File data is a tuple (name, contents)
		file_data = file_parser.load_file(directory + "/" + path)
		if file_data:
			# Gather results
			file_results = file_parser.get_results(file_data[1])
			file_results['name'] = file_data[0]
			file_results['path'] = directory + "/" + path
			file_results['sentiment'] = classifier.classify_text(file_data[1])
			# Save to database
			database.insert_file(file_results)

	database.db.close()