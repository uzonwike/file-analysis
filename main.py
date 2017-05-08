from os import listdir
from os.path import isfile, join, abspath, basename
import file_parser
from sentiment_classifier import *
import database
import peewee
from multiprocessing import Pool

NUM_THREADS = 6

# Save results in the database
def process_results(file_result):
	if file_result:
		# Save to database
		try:
			database.insert_file(file_result)
		except peewee.IntegrityError:
			pass
			# print("File already exists in the database.")

# Analyze files
def analyze_files(directory, save_to_db = True):
	# Get all file paths, load the classifier
	try:
		paths = [f for f in listdir(directory) if isfile(join(directory, f))]
	except WindowsError:
		print("No such directory exists.")
	else:
		# Create the classifier
		classifier = FileClassifier()

		# Open all files in dir with threads
		database.db.connect()
		p = Pool(NUM_THREADS)
		paths = [(directory + "/" + path) for path in paths]
		results = p.map(file_parser.load_file, paths)

		# Get file results
		file_results = []
		for file_data in results:
			# Gather results
			file_result = file_parser.get_results(file_data[1])
			file_result['name'] = basename(file_data[0])
			file_result['path'] = abspath(file_data[0])
			file_result['sentiment'] = classifier.classify_text(file_data[1])
			file_results.append(file_result)

		# Save file results to DB
		p = Pool(NUM_THREADS)
		p.map(process_results, file_results)

		database.db.close()

if __name__ == '__main__':
	d = raw_input("Enter a directory of files to perform analysis on: ")
	analyze_files(d)