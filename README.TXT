This project contains two programs.

1) The file analyzer
This program analyzes a given directory, determining statistics about each file in the directory such as the sentiment, and word count. This program is run through main.py.

2) The display console
This program gives the user access to a simple shell. This shell can be used to display information about files in the database that have been previously analyzed and stored. This program is run through display.py.

Requirements:
There are multiple Python dependencies that are required to run either of the programs. They can all be installed by using pip.
Install SciPy
Install peewee
Install nltk
Install sklearn

References:
We used the movie review data set, www.cs.cornell.edu/people/pabo/movie-review-data/, taken from Learning Word Vectors for Sentiment by Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, and Christopher Potts.

Additionally, parts of the classifier were created by following the tutorial found at: https://marcobonzanini.com/2015/01/19/sentiment-analysis-with-python-and-scikit-learn/.