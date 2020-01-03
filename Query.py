import json
import sys
from collections import Counter
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

indexing = sorted_indexing = result = {}
query_text = stemmer.stem(' '.join(sys.argv[1:]))
query = dict(Counter(query_text.split()))

with open('indexing.json') as f:
    indexing = json.loads(f.read())

for w, c in query.items():
    if w not in indexing:
        continue

    sorted_indexing = sorted(indexing[w].items(), key=lambda x: x[1], reverse=True)

    for doc, score in sorted_indexing:
        if doc in result:
            result[doc] += float(score) * c
        else:
            result[doc] = float(score)

results = sorted(result.items(), key=lambda x: x[1], reverse=True)
# print(type(results))

selected_docs = {}
rank = 0
directory = './Processing/clean/'
for doc,score in results:
    with open(directory+doc+'.txt') as f:
        lines = f.read().split('\n')
        selected_docs[rank] = {
            'score' : score,
            'title' : lines[0],
            'desc' : lines[1],
            'body' : lines[2],
            'url' : lines[3],
        }
        rank += 1

print(json.dumps(selected_docs))
