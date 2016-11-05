import filenames
import fnmatch
import os
import itertools
from nltk.tokenize import wordpunct_tokenize
import numpy as np
import random
def gen_sens(eng,m,n):
    res = []
    words = wordpunct_tokenize(eng)
    for i in range(0,m-4):
        perm = []
        
        perm = list(np.random.permutation(words))
        ans = ''
        for j in range(0,len(perm)):
            ans = ans+" "+perm[j]
        res.append(ans)

    with open('../sample.txt') as f:
        sample = f.read().splitlines()

    s = random.randint(0,len(sample)-n-1)
    for i in range(s,s+n):
        res.append(sample[i])

    idx = random.randint(0,len(words)-1)
    ans = ''
    for j in range(0,len(words)):
        if j != idx:
            ans = ans+words[j]
    res.append(ans)
    for i in range(0,3):
        idx = random.randint(0,len(words)-1)
        perm = list(np.random.permutation(words))
        ans = ''
        for j in range(0,len(perm)):
            if j != idx:
                ans = ans+perm[j]
        res.append(ans)
        
    return res


def gen_test_cases(m,n,fname,ename,rname):
    print "Generating test cases "
    count = 0
    rese = open(ename,'w')
    resf = open(rname,'w')
    new_dict = dict()
    for file in os.listdir(fname):
        
        if count >= 1000:
            break
        if fnmatch.fnmatch(file,'*.f'):
            print file
            efile = file[:-2]+'.e'
            with open(fname+file) as f :
                french = f.read().splitlines()
            with open(fname+efile) as f:
                english = f.read().splitlines()

            for i in range(0, len(french)):
                resf.write(french[i]+'\n')
                res = gen_sens(english[i],m,n)
                res.append(english[i])
                for j in range(0,len(res)):
                    rese.write(res[j]+'\n')
                new_dict[french[i]] = res
                if(count >= 1000):
                    break
                count = count + 1

    return new_dict

def main():
    gen_test_cases(20,20,filenames.HOUSE_TRAINING,'../testcasese.txt','../testcasesf.txt')
    gen_test_cases(20,20,filenames.SENATE_TRAINING,'../testcasesse.txt','../testcasessf.txt')
main()
