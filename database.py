from __future__ import print_function
# The connection to the dabase
from peewee import *

db = SqliteDatabase('files.db')

# This model stores all the fields from a file that has been analyzed 
class File(Model):
    name = CharField()
    directory = CharField()
    word_count = IntegerField()
    sentiment = CharField()

    class Meta:
        database = db

# Print all the specified attrs of a list of files
def print_files(files, attrs):
	for file in files:
		data = vars(file)["_data"]
		for attr in attrs:
			s = attr + " is " + str(data[attr])
			if attr == "name":
				print(data[attr] + " ")
			elif attr != attrs[-1]:
				print(s, end=", ")
			else:
				print(s + ".")
		print()

# Print the data for a specific file
def print_file_data(name, directory):
	try:
		file = File.select().where(File.name == name).where(File.directory == directory).get()
		print_files([file], [attr for attr in vars(file)["_data"]])
	except Exception as e:
		print(e.__class__.__name__)

db.connect()
print_files(File.select(), ["name", "directory", "sentiment", "word_count"])
db.close()