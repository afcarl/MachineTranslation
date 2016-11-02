import collections
from nltk.tokenize import wordpunct_tokenize

def bigramgen(filename):
    file = open(filename,"r")
    bigrams = collections.Counter()

    for line in file:
        line = line.lower()
        line = line.strip()
        words = wordpunct_tokenize(line)
        for i in range(2,len(words)):
            bigram = words[i-1]+'_'+words[i]
            bigrams[bigram] += 1

    return bigrams

