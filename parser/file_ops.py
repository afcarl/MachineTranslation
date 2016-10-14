import collections 

def read_vocab(filename):
	file = open(filename, "r")
	words = dict()

	for line in file:
		items = line.split()
		words[items[0].strip()] = int(items[1].strip())

	vocab = collections.Counter(words)

	return vocab

def write_vocab(vocab,filename):

	with open(filename,"w") as f:
		for key,value in vocab.most_common():
			f.write("{} {}\n".format(key,value))




