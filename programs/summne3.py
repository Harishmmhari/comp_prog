def breakingRecords(scores):
    mi=scores[0]
    ma=scores[0]
    minn=0
    maxn=0
    for i in scores:
        if i > ma:
            maxn=maxn+1
            ma=i
        if i< mi:
            minn=minn+1
            mi=i
    print(maxn,minn)

breakingRecords([10,5,20,20,4,5,2,25,1])