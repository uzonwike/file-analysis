from os import listdir
from os.path import isfile, join
import file_parser
from sentiment_classifier import *
import database
import threading
from multiprocessing import Queue
from multiprocessing.dummy import Pool

directory = "/home/uzonwike/Documents/CSC213/file-analysis/data/"
paths = [f for f in listdir(directory) if isfile(join(directory, f))]
classifier = FileClassifier()
print "YAAAH"
def analyze_files(directory):
	# Get all file paths, load the classifier
	#paths = [f for f in listdir(directory) if isfile(join(directory, f))]
	#classifier = FileClassifier()

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

q = Queue()
lock = threading.Lock()

#Put all file paths in a queue
for f in listdir(directory):
	if isfile(join(directory, f)):
		q.put(join(directory, f))
		print f
#q.join()    #block until all tasks are complete

def do_work(item):
    with lock:
        print(item)    #will print file path
    fh = open (item)
    src = fh.read()

def worker():
    while True:
        item = q.get()
        try:
            do_work(item)
        except Exception as e:
            print(e)
        finally:
            q.task_done()

for i in range(4):
    t = threading.Thread(target=worker)
    t.daemon = True
#    t.start()

#for i in xrange(len(paths)):
#    paths[i] = directory + "/" + paths[i]


# p = Pool() # automatically scales to the number of CPUs available
# results = p.map(analyze_files("/home/uzonwike/Documents/CSC213/file-analysis/data/"), paths)
# p.close()
# p.join()


analyze_files("/home/uzonwike/Documents/CSC213/file-analysis/data/")