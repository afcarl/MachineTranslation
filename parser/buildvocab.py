import collections
from tokengen import tokengen
import filenames
import fnmatch
import os

def buildvocab():

	# English Vocabulary
	vocab_e = collections.Counter()

	#French Vocabulary
	vocab_f = collections.Counter()

	# Building  Vocabulary from House Data
	print 'Building vocabualry for House Data'
	for file in os.listdir(filenames.HOUSE_TRAINING):
		if fnmatch.fnmatch(file,'*.e'):
			print file
			result = tokengen(filenames.HOUSE_TRAINING+file)
			vocab_e = vocab_e + result
		elif fnmatch.fnmatch(file,'*.f'):
			print file
			result = tokengen(filenames.HOUSE_TRAINING+file)
			vocab_f = vocab_f + result

	
	# Building Vocabulary for Senate Data
	print 'Building vocabulary for Senate Data'
	for file in os.listdir(filenames.SENATE_TRAINING):
		if fnmatch.fnmatch(file,'*.e'):
			print file
			result = tokengen(filenames.SENATE_TRAINING+file)
			vocab_e = vocab_e + result
		elif fnmatch.fnmatch(file,'*.f'):
			print file
			result = tokengen(filenames.SENATE_TRAINING+file)
			vocab_f = vocab_f + result



def main():
	buildvocab()

main()
