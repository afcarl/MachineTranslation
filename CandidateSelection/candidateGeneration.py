import itertools
import random
import math
import numpy
from itertools import combinations
from random import randint

def candidateGeneration(str, n, totalCandidateCount):
	
	words = str.lower().split()
	res = []
	index = 0
	
	while(index < len(words)):
		permutation = []
		increment = randint(1,n)
		sublist = words[index:index+increment]
		index = index + increment
		permutation += [' '.join(x) for x in itertools.permutations(sublist)]
		res.append(permutation)

	candidates = []
	upperLimit = int(math.ceil(math.sqrt(totalCandidateCount)))
	for i in range(1,upperLimit):
		line = ""
		for elem in res:
			line += random.choice(elem) + " "
		candidates.append(line.strip());
	
	return candidates

def candidateSentenceGeneration(select_matrix,prob_matrix, n, totalCandidateCount):

	candidates = []
	upperLimit = int(math.ceil(math.sqrt(totalCandidateCount)))
	for i in range(1,upperLimit):
		line = ""
		listIndex = 0
		for elem in select_matrix:
			line += numpy.random.choice(elem, p=prob_matrix[listIndex]) + " "			
			listIndex = listIndex + 1

		candidates += candidateGeneration(line.strip(),n, totalCandidateCount);

	#print(candidates)
	return candidates
		

def main():	
	#candidateGeneration("The recommended way to install Eclipse on Ubuntu is using the distribution's package manager", 4, 1000)

	select_matrix = [['The' ,'A', 'An','Sample'],['recommended'],['way','thing'],['to'],['install'],['Eclipse'],['on'],['Ubuntu'],['is'],['using'],['the'],['distribution', 'distribute'],['package'],['manager']]


	prob_matrix = [[0.5,0.3,0.1,0.1],[1],[0.6,0.4],[1],[1],[1],[1],[1],[1],[1],[1],[0.5,0.5],[1],[1]];

	candidateSentenceGeneration(select_matrix,prob_matrix,3,1000)
	

main()
