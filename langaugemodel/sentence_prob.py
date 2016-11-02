from __future__ import division
import collections
from file_ops import read_trigrams
import filenames
from nltk.tokenize import wordpunct_tokenize
import math

def sentence_prob(s):
    trigram_e = read_trigrams(filenames.TRIGRAM_ENGLISH)
    bigram_e = read_trigrams(filenames.BIGRAM_ENGLISH)

    b_total = len(bigram_e.keys())
    print "Files Read"
    print "Total Number of bigrams : ",b_total
    s = s.lower();
    s = s.strip();
    words = wordpunct_tokenize(s)
    tprob = 0
    for i in range(3,len(words)):
        tcount = trigram_e[words[i-2]+'_'+words[i-1]+'_'+words[i]]
        bcount = bigram_e[words[i-2]+'_'+words[i-1]]
        
        prob = (tcount+1)/(bcount+b_total);
        lprob = math.log(prob)
        tprob += lprob

    return tprob

def main():
    prob = sentence_prob("It is indeed a great honour to be entrusted with this task.")
    print "Log prob is : ",prob
main()
