import collections
from nltk.tokenize import wordpunct_tokenize

def trigramgen(filename):
    file = open(filename,"r")
    trigrams = collections.Counter()

    for line in file:
        line = line.lower()
        line = line.strip()
        words = wordpunct_tokenize(line)
        for i in range(3,len(words)):
            trigram = words[i-2]+'_'+words[i-1]+'_'+words[i]
            trigrams[trigram] += 1

    return trigrams

