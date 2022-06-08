from sys import stdin
for line in stdin:
    museos = input().split()
    mMe = mMa = int(museos[0])
    for i in museos:
        if int(i) > mMa:
            mMa = int(i)
        if int(i) < mMe:
            mMe = int(i)
    print(mMa-mMe)