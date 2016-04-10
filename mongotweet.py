# Twitter Data from MongoDB
#                       Pavan Narayanan, 2016

# Connect to MongoDB
import json
import pandas as pd
import numpy as np
from pymongo import MongoClient
from nltk import word_tokenize
client = MongoClient('localhost',27017)
db = client['twitterdata']
collection = db['twitter1']

# Extract just one
query0 = db.twitter1.find_one()
# print json.dumps(query0))

# for key,value in query0:
#    print query0.values

# Extract only the tweets
query1 = db.twitter1.find({},{"text":1,"_id":0})
query2 = db.twitter1.find({},{"user.location":1,"text":1,"_id":0})
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
a = listq2[2]
print word_tokenize(a)