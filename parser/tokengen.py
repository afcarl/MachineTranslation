import collections
import re

def tokengen(file):
	with open(file) as f:
	    	tokens = collections.Counter(
				word.lower()
				for line in f
				for word in re.findall(r'\b[^\W\d_]+\b', line))
	return tokens

