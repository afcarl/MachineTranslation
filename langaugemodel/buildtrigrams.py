import collections
from trigramgen import trigramgen
from bigramgen import bigramgen
import filenames
import fnmatch
import os
from file_ops import write_trigrams, read_trigrams

def buildtrigrams():

	# English Vocabulary
	trigram_e = collections.Counter()

	#French Vocabulary
	trigram_f = collections.Counter()

	# Building  Vocabulary from House Data
	print 'Building vocabualry for House Data'
	for file in os.listdir(filenames.HOUSE_TRAINING):
		if fnmatch.fnmatch(file,'*.e'):
			result = trigramgen(filenames.HOUSE_TRAINING+file)
			trigram_e = trigram_e + result
	#	elif fnmatch.fnmatch(file,'*.f'):
	#		print file
			#result = trigramgen(filenames.HOUSE_TRAINING+file)
			#trigram_f = trigram_f + result

	
	# Building Vocabulary for Senate Data
	print 'Building vocabulary for Senate Data'
	for file in os.listdir(filenames.SENATE_TRAINING):
		if fnmatch.fnmatch(file,'*.e'):
			result = trigramgen(filenames.SENATE_TRAINING+file)
			trigram_e = trigram_e + result
	#	elif fnmatch.fnmatch(file,'*.f'):
	#		print file
	#		#result = trigramgen(filenames.SENATE_TRAINING+file)
	#		#trigram_f = trigram_f + result

	write_trigrams(trigram_e,filenames.TRIGRAM_ENGLISH)	
	
        #write_trigrams(trigram_f,filenames.TRIGRAM_FRENCH)
def buildbigrams():

        bigram_e = collections.Counter()
        print "Building bi grams fro House Data"

        for file in os.listdir(filenames.HOUSE_TRAINING):
		if fnmatch.fnmatch(file,'*.e'):
			result = bigramgen(filenames.HOUSE_TRAINING+file)
			bigram_e = bigram_e + result
	#	elif fnmatch.fnmatch(file,'*.f'):
	#		print file
			#result = trigramgen(filenames.HOUSE_TRAINING+file)
			#trigram_f = trigram_f + result

	
	# Building Vocabulary for Senate Data
	print 'Building vocabulary for Senate Data'
	for file in os.listdir(filenames.SENATE_TRAINING):
		if fnmatch.fnmatch(file,'*.e'):
			result = bigramgen(filenames.SENATE_TRAINING+file)
			bigram_e = bigram_e + result
	#	elif fnmatch.fnmatch(file,'*.f'):
	#		print file
	#		#result = trigramgen(filenames.SENATE_TRAINING+file)
	#		#trigram_f = trigram_f + result

	write_trigrams(bigram_e,filenames.BIGRAM_ENGLISH)	
	
def main():
#	buildtrigrams()
        buildbigrams()
main()
