import re

# Takes file and returns a 2-tuple containing a string of the file name, and the file contents
def load_file(file_name):
	with open(file_name) as f:
		name = file_name
		contents = f.read()
		separations = ['\n', '\t']
		for ch in separations:
			if ch in contents:
				contents = contents.replace(ch, ' ')
		re.sub(r'[^\w]', ' ', contents)
		return (name, contents)

# Get file metadata
def get_results(string_of_file):
	results = {}
	return results