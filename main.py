from os import listdir
from os.path import isfile, join, abspath, basename
import file_parser
from sentiment_classifier import *
import database
import peewee

def analyze_files(directory, save_to_db = True):
	# Get all file paths, load the classifier
	paths = []
	try:
		paths = [f for f in listdir(directory) if isfile(join(directory, f))]
	except WindowsError:
		print("No such directory exists.")
	finally:
		classifier = FileClassifier()

		# Do analysis for all files in dir
		database.db.connect()
		for path in paths:
			# File data is a tuple (name, contents)
			file_data = file_parser.load_file(directory + "/" + path)
			if file_data:
				# Gather results
				file_results = file_parser.get_results(file_data[1])
				file_results['name'] = basename(file_data[0])
				file_results['path'] = abspath(file_data[0])
				file_results['sentiment'] = classifier.classify_text(file_data[1])
				# Save to database
				try:
					if save_to_db:
						database.insert_file(file_results)
				except peewee.IntegrityError:
					print("File already exists in the database.")

		database.db.close()

analyze_files("C:\\Users\\Marcel\\file-analysis\\")