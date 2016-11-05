

def combinations(l,idx):
    if idx == (len(l) - 1) :
        return l[idx]

    res = []
    tlist = combinations(l,idx+1)
    for i in range(0,len(tlist)):
        temp = tlist[i]
        for j in range(0,len(l[idx])):
            rval = l[idx][j]+" "+temp
            res.append(rval)

    return res

def main():
    l1 = ['this','the','mallfunction']
    l2 = ['hell','is','what']
    l3 = ['no','nada','gen']
    l = []
    l.append(l1)
    l.append(l2)
    l.append(l3)

    res = combinations(l,0)
    print res

main()

