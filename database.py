from __future__ import print_function
# The connection to the dabase
from peewee import *

db = SqliteDatabase('files.db')

# This model stores all the fields from a file that has been analyzed 
class File(Model):
    path = CharField(unique=True)
    word_count = IntegerField()
    char_count = IntegerField()
    sentiment = CharField()
    name = CharField()

    class Meta:
        database = db

# Insert a file
def insert_file(file_dict):
	File.create(**file_dict)

# Print all the specified attrs of a list of files
def print_files(files, attrs, table = True):
	if files.count() == 0:
		print("No files found.")
	# Print the header, using string formatting
	if files and table:
		header = vars(files[0])["_data"]
		print(("{:<25}"*len(header)).format(*header))
	for file in files:
		data = vars(file)["_data"]
		# If we are printing as a table
		# Print each file as a row
		if table:
			values = []
			for v in data.values():
				if type(v) == unicode and len(v) > 20:
					values.append("..." + v[-17:])
				else:
					values.append(v)
			print(("{:<25}"*len(data)).format(*values))
		# Otherwise, print as formatted sentence
		else:
			for attr in attrs:
				s = attr + " is " + str(data[attr])
				if attr == "name":
					print(data[attr] + " ")
				elif attr != attrs[-1]:
					print(s, end=", ")
				else:
					print(s + ".")
			print()

# Print the files whose path contains the specified path
def print_files_path_contains(path, table = True):
	files = File.select().where(File.path.contains(path))
	print_files(files, ["name", "path", "sentiment", "word_count", "char_count"], table = table)

# Print the data for a specific file
def print_file_data(path, table = False):
	files = File.select().where(File.path == path)
	if files.count() > 0:
		print_files(files, [attr for attr in vars(files.get())["_data"]], table = table)
	else:
		print("The specified file does not exist.")

# Print all files in the database
def print_all_files(table = True):
	print_files_path_contains("", table = table)

# Print the files whose path contains the specified path
def print_files_with_sentiment(sentiment, table = True):
	files = File.select().where(File.sentiment == sentiment)
	print_files(files, ["name", "path", "sentiment", "word_count", "char_count"], table = table)