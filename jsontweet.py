# Reading JSON output
# Pavan Narayanan, 2016
#

import json
from nltk import word_tokenize
import codecs
from collections import Counter
tlist = []

with open('/home/hdanalytics/tweets1.json', 'r') as tweetfile:
    wordcount = Counter()
    for line in tweetfile:
        tweet = json.loads(line)
        token = word_tokenize(tweet['text'])
        tlist.append(token)
        print token
    #finaltlist = word_tokenize(tlist)
    #wordcount.update(finaltlist)
    #print wordcount.most_common(10)

    # print(json.dumps(tweetdict,indent=4))
# print tweetdict.get('text')
# print word_tokenize(tweetdict.get('text'))
# print (word_tokenize(tweetdict))

