import os
import math
import json
from collections import Counter

# bagOfWords = {}
TFs = {}
DFs = {}
directory = './stemmed/'
listdir = os.listdir(directory)
for file in listdir:
    idDoc = file.replace('.txt', '')
    TFs[idDoc] = {}

    with open(directory+file, 'r') as f:
        lines = f.read().split('\n')

        title = Counter(lines[0].split())
        desc = Counter(lines[1].split())
        body = Counter(lines[2].split())
        all_text = title + desc + body

        word_count = len(list(all_text.elements()))

        TFs[idDoc]['title'] = {w: (c/word_count) * 0.5 for w,c in title.items()}
        TFs[idDoc]['desc'] = {w: (c/word_count) * 0.3 for w,c in desc.items()}
        TFs[idDoc]['body'] = {w: (c/word_count) * 0.2 for w,c in body.items()}

        # bagOfWords[idDoc] = dict(title + desc + body)

        for w in all_text:
            try:
                DFs[w].add(idDoc)
            except:
                DFs[w] = {idDoc}


doc_count = len(listdir)
IDFs = {w: math.log10(doc_count/len(ids)) for w,ids in DFs.items()}

# print(IDFs)

TFIDFs = {}

with open('../indexing.json', 'w') as f:
    for widf,idf in IDFs.items():
        TFIDFs[widf] = {}
        for idDoc,tf in TFs.items():

            title = (tf['title'][widf] if widf in tf['title'] else 0) * idf
            desc = (tf['desc'][widf] if widf in tf['desc'] else 0) * idf
            body = (tf['body'][widf] if widf in tf['body'] else 0) * idf

            TFIDF = title + desc + body
            if(title or desc or body):
                TFIDFs[widf][idDoc] = title + desc + body

    json.dump(TFIDFs, f)