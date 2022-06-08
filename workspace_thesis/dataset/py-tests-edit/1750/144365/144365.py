import re
from unicodedata import normalize

while True:
    s=str(input())
    s=re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
        normalize( "NFD", s), 0, re.I)
    a=len(s)//2
    f=len(s)-1
    r=""
    r2=""
    c=0
    for i in range(0,a,1):
        r+=s[i]
        r2=s[f-i]+r2
        if r==r2:
            c+=1
    if c>0:
        print("si")
    else:
        print("no")
