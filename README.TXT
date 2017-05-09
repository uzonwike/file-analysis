Description:
This is a file analysis tool that processes files using natural language processing. Our program processes directories in parallel using threading and produces sentiment results along with basic statistics. After the directory is analyzed, we catalog the
results of each file in a database in order to persist the data. The tool can also be used to output information about the files that have been cataloged.

The system has two components:

1) The file analyzer (main.py)
This program analyzes a given directory, determining statistics about each file in the directory such as the sentiment, and word count.

2) The display console (display.py)
This program gives the user access to a simple shell. This shell can be used to display information about files in the database that have been previously analyzed and stored.

Running the Project:
As this is a Python project, there is no MAKE file. You must simply install the following Python packages since they are required to run either of the programs. All of the packages can be installed by using pip. Following the installation of the dependencies, you can simply run main.py or display.py from the console.

List of dependencies:
1) Install SciPy
2) Install peewee
3) Install nltk
4) Install sklearn

Note: classification takes a long time so analyzing large folders/files is not recommended.

Examples:

main.py
Enter a directory of files to perform analysis on: ./data/verify/
Creating corpus...
Calculating results...
Classified neg1.txt as neg.
Classified neg2.txt as neg.
Classified neg3.txt as neg.
Classified neg4.txt as neg.
Classified pos1.txt as pos.
Classified pos2.txt as pos.
Classified pos3.txt as pos.
Classified pos4.txt as pos.
Classified pos5.txt as pos.

display.py
Type 'commands' to see the list of available commands
> commands
The following commands are available:
1. list (list all files)
2. sentiment <sentiment> (list all files of with a sentiment of <sentiment>)
3. path <path> (list all files where the file's path contains <path>)
4. data <path> (list the data of file with path of <path>)
5. table (toggle table format on/off)

> list
name                     sentiment                char_count               word_count               path                     id
neg1.txt                 neg                      100                      20                       ...a\verify\neg1.txt     1
neg2.txt                 neg                      147                      30                       ...a\verify\neg2.txt     2
neg3.txt                 neg                      124                      25                       ...a\verify\neg3.txt     3
pos5.txt                 pos                      104                      19                       ...a\verify\pos5.txt     4
pos3.txt                 pos                      29                       6                        ...a\verify\pos3.txt     5
pos4.txt                 pos                      179                      37                       ...a\verify\pos4.txt     6
pos2.txt                 pos                      75                       17                       ...a\verify\pos2.txt     7
neg4.txt                 neg                      185                      37                       ...a\verify\neg4.txt     8
pos1.txt                 pos                      56                       13                       ...a\verify\pos1.txt     9
> sentiment positive
No files found.
> sentiment pos
name                     sentiment                char_count               word_count               path                     id
pos5.txt                 pos                      104                      19                       ...a\verify\pos5.txt     4
pos3.txt                 pos                      29                       6                        ...a\verify\pos3.txt     5
pos4.txt                 pos                      179                      37                       ...a\verify\pos4.txt     6
pos2.txt                 pos                      75                       17                       ...a\verify\pos2.txt     7
pos1.txt                 pos                      56                       13                       ...a\verify\pos1.txt     9
> sentiment neg
name                     sentiment                char_count               word_count               path                     id
neg1.txt                 neg                      100                      20                       ...a\verify\neg1.txt     1
neg2.txt                 neg                      147                      30                       ...a\verify\neg2.txt     2
neg3.txt                 neg                      124                      25                       ...a\verify\neg3.txt     3
neg4.txt                 neg                      185                      37                       ...a\verify\neg4.txt     8
> path verify\
name                     sentiment                char_count               word_count               path                     id
neg1.txt                 neg                      100                      20                       ...a\verify\neg1.txt     1
neg2.txt                 neg                      147                      30                       ...a\verify\neg2.txt     2
neg3.txt                 neg                      124                      25                       ...a\verify\neg3.txt     3
pos5.txt                 pos                      104                      19                       ...a\verify\pos5.txt     4
pos3.txt                 pos                      29                       6                        ...a\verify\pos3.txt     5
pos4.txt                 pos                      179                      37                       ...a\verify\pos4.txt     6
pos2.txt                 pos                      75                       17                       ...a\verify\pos2.txt     7
neg4.txt                 neg                      185                      37                       ...a\verify\neg4.txt     8
pos1.txt                 pos                      56                       13                       ...a\verify\pos1.txt     9
> path neg
name                     sentiment                char_count               word_count               path                     id
neg1.txt                 neg                      100                      20                       ...a\verify\neg1.txt     1
neg2.txt                 neg                      147                      30                       ...a\verify\neg2.txt     2
neg3.txt                 neg                      124                      25                       ...a\verify\neg3.txt     3
neg4.txt                 neg                      185                      37                       ...a\verify\neg4.txt     8
> help
The following commands are available:
1. list (list all files)
2. sentiment <sentiment> (list all files of with a sentiment of <sentiment>)
3. path <path> (list all files where the file's path contains <path>)
4. data <path> (list the data of file with path of <path>)
5. table (toggle table format on/off)

> table
Display as table: False
> sentiment neg
neg1.txt
path is C:\Users\Marcel\file-analysis\data\verify\neg1.txt, sentiment is neg, word_count is 20, char_count is 100.

neg2.txt
path is C:\Users\Marcel\file-analysis\data\verify\neg2.txt, sentiment is neg, word_count is 30, char_count is 147.

neg3.txt
path is C:\Users\Marcel\file-analysis\data\verify\neg3.txt, sentiment is neg, word_count is 25, char_count is 124.

neg4.txt
path is C:\Users\Marcel\file-analysis\data\verify\neg4.txt, sentiment is neg, word_count is 37, char_count is 185.

References:
We used the movie review data set, www.cs.cornell.edu/people/pabo/movie-review-data/, taken from Learning Word Vectors for Sentiment by Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, and Christopher Potts.

Additionally, parts of the classifier were created by following the tutorial found at: https://marcobonzanini.com/2015/01/19/sentiment-analysis-with-python-and-scikit-learn/.