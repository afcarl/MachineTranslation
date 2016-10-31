import nltk
from nltk import ngrams
from nltk.corpus import brown


def generate_trigram_freq_map():
	#map containing freq for each trigram
	map = {}

	# Getting all words from brown corpus
	words =(t.encode("ascii","ignore") for t in (w.lower() for w in brown.words()))

	#n-gram generation
	trigrams = ngrams(words, 3)

	freqDist = nltk.FreqDist(trigrams)
	
	print("Calculation Freq : ")
	for sample in freqDist:
		print(sample)
		map[sample] = freqDist.freq(sample) / freqDist.N()

	#write map to file
	write_trigram_freq("../freq.txt",map)


def write_trigram_freq(filename, map):

	with open(filename,"a") as f:
		for k,v in map.items():
			f.write("{},{}\n".format(k,v))

def main():
	generate_trigram_freq_map()

main()
