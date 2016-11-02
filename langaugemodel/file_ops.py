import collections 

def read_trigrams(filename):
	file = open(filename, "r")
	words = dict()

	for line in file:
		items = line.split()
		words[items[0].strip()] = int(items[1].strip())

	vocab = collections.Counter(words)

	return vocab

def write_trigrams(trigrams,filename):

	with open(filename,"w") as f:
		for key,value in trigrams.most_common():
			f.write("{} {}\n".format(key,value))




