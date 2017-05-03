from os import listdir
from os.path import isfile, join
import loader

def load_files(directory):
	paths = [f for f in listdir(directory) if isfile(join(directory, f))]
	for path in paths:
		file_data = load_file(path)
		if file_data:
			# Send to classifier
			# Get sentiment results
			# Save sentiments results and file data (e.g more stuff we manually parse like # of words)
			pass



load_files(".")
