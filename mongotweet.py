# Twitter Data from MongoDB
#                       Pavan Narayanan, 2016
# Connect to MongoDB

from pymongo import MongoClient
from nltk import word_tokenize
import itertools
from collections import Counter
from nltk.corpus import stopwords
import string

client = MongoClient('localhost', 27017)
db = client['twitterdata']
collection = db['twitter1']

# Extract just one
query0 = db.twitter1.find_one()
# print json.dumps(query0))

# for key,value in query0:
#    print query0.values
# Extract only the tweets
query1 = db.twitter1.find({}, {"text": 1, "_id": 0})
query2 = db.twitter1.find({}, {"user.location": 1, "text": 1, "_id": 0})
# print type(query1)

# df = pd.DataFrame(query1)
# pd1 = pd.read_json(query1)

listq1 = []
listq2 = []
for document in query1:
    listq1.append(document)

for document in query2:
    listq2.append(document)

# Do a word count
a = word_tokenize(str(listq1[1]), language='english')

newlist = []

for line in listq1:
    newlist.append(word_tokenize(str(line), language='english'))

# flatten the list
flatnewlist = list(itertools.chain(*newlist))

wordCount = Counter(list(itertools.chain(*newlist)))
# print wordCount

# prepare a list of words to remove
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']

# remove the words from flattened list
nremove = [x for x in flatnewlist if x not in stop]

# do a word count on that flattened list
wordCount1 = Counter(nremove)

f1 = open('newlist1.txt', 'w')
print >>f1, wordCount1
#print punctuation

#f1.write('wordCount1')
# print wordCount1
