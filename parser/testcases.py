import filenames
import fnmatch
import os
import itertools
from nltk.tokenize import wordpunct_tokenize

def gen_sens(eng,m,n):
    sample = ['Tobacco Industry Responsibility Bill',
            "Second Reading-Points of Order-Speaker's Ruling",
            'Referred to Committee',
            'Transport and Communication',
            'Motion to Authorize Committee to Meet During Sittings of the Senate-Order Withdrawn',
            'The Senate',
            'Lack of Accessibility for Disabled to Facilities-Inquiry-Debate Concluded',
            'Inter-Provincial Relations',
            'Applicability of Subpoenas Issued in Relation to Commissions of Inquiry-Motion-Debate Adjourned',
            'Aboriginal Peoples',
            'First Nations Government Bill-Committee Authorized to Apply Materials and Evidence Gathered on Examination of Previous Bills to Study of Current Bill',
            'Business of the Senate']
    res = []
    words = wordpunct_tokenize(eng)
    for i in range(0,m):
        for j in range(1,len(words)):
            temp = words[j]
            words[j] = words[j-1]
            words[j-1] = temp
        ans = ''
        for j in range(0,len(words)):
            ans = ans+words[j]
        res.append(ans)

    for i in range(0,n):
        res.append(sample[i])
    return res


def gen_test_cases(m,n):
    print "Generating test cases "
    count = 0
    resf = open('../testcase.txt','w')

    new_dict = dict()
    for file in os.listdir(filenames.HOUSE_TRAINING):
        
        if count > 100:
            break;
        if fnmatch.fnmatch(file,'*.f'):
            efile = file[:-2]+'.e'
            with open(filenames.HOUSE_TRAINING+file) as f :
                french = f.read().splitlines()
            with open(filenames.HOUSE_TRAINING+efile) as f:
                english = f.read().splitlines()


            for i in range(0, len(french)):
                resf.write(french[i]+'\n')
                resf.write(english[i]+'\n')
                res = gen_sens(english[i],m,n)
                for j in range(0,len(res)):
                    resf.write(res[j]+'\n')
                res.append(english[i])
                new_dict[french[i]] = res
                if(count >= 100):
                    break
                count += 1

    return new_dict

def main():
    gen_test_cases(2,3)

main()
