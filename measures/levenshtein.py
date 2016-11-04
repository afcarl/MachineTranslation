
from nltk.tokenize import wordpunct_tokenize

# Credits : https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python

def levenshtein(s1,s2):
    w1  = wordpunct_tokenize(s1) 
    w2  = wordpunct_tokenize(s2)

    if len(w1) < len(w2):
        return levenshtein(s2,s1)

    if len(w2) == 0:
        return len(w1)

    previous_row = range(len(w2) + 1)
    for i, c1 in enumerate(w1):
        current_row = [i+1]
        for j,c2 in enumerate(w2):
            insertions = previous_row[j+1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions,deletions,substitutions))
        previous_row = current_row

    return previous_row[-1]


def main():
    s1= "This is lol max"
    s2= "This is lol"
    w = levenshtein(s1,s2)
    print "value", w

main()
