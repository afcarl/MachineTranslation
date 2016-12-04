import heapq
import random

def candidateGeneration(vocab, totalCandidatesCount):
	STOP = "$"
	heapsize = totalCandidatesCount

	heap = []
	heappush(heap,(0,STOP),heapsize)
	#initial setup
	extendPhrase("",vocab, heap, STOP, heapsize)

	#print heap
	print "\n"

	candidates = []
	
	while heap:
		tuplePair = heappop(heap)		

		if tuplePair[1].find(STOP)!=-1:
			candidates.append(tuplePair)
		else:
			extendPhrase(tuplePair[1], vocab, heap, STOP, heapsize)

	
	heap = list(candidates)
	heapq.heapify(heap)
	#print len(candidates)
	return heap


def extendPhrase(phrase, vocab, heap, STOP, heapsize):
	
	for elem in vocab:
		if phrase.find(elem)==-1:
			temp = phrase + " " + elem
			heappush(heap,(phraseScore(temp.strip())*-1,temp.strip()),heapsize)
			temp = temp + " " + STOP
			heappush(heap,(phraseScore(temp.strip())*-1, temp.strip()),heapsize)


def heappush(heap, tuplePair, heapSize):

	if len(heap) < heapSize:
		heapq.heappush(heap, tuplePair)
	else:
		heap[heapSize-1] = tuplePair
		heapq.heapify(heap)

def heappop(heap):
	return heapq.heappop(heap)	

def phraseScore(phrase):
	return random.random()


def main():
	candidateGeneration(["the","wizard","of","oz"],10)

main()
