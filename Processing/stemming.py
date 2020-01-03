import os
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# create stopword remover
swrFactory = StopWordRemoverFactory()
stopword = swrFactory.create_stop_word_remover()

directory = './clean/'
stemmed_log = {}
with open ('stemmed_log.txt', 'r') as sl:
    raw_stemmed_log = sl.readlines()
    stemmed_log = {i : 0 for i in raw_stemmed_log}

with open('stemmed_log.txt', 'a+') as sl:
    for file in os.listdir(directory):
        full_path = directory+file

        if full_path in stemmed_log:
            print('continue:', full_path)
            continue

        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read().split('\n')

            with open('./stemmed/'+file, 'a+') as sf:
                for line in content[0:3]:
                    stemmed = stemmer.stem(line)
                    removed = stopword.remove(stemmed)
                    sf.write(removed+'\n')

            # log
            sl.write(f.name+'\n')
            stemmed_log[f.name] = 0
            print(file, f.name)
