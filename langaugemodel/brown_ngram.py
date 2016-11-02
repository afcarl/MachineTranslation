from collections import Counter

from nltk.corpus import brown
from nltk.util import ngrams

n = 3
bigrams = ngrams(brown.words(), n)
bigrams_freq = Counter(bigrams)

print bigrams_freq[('chocolate', 'milkshake','is')]
print bigrams_freq.most_common()[2000]
