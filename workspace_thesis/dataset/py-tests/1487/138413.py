import math
from sys import stdin
def primo(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True
    
for a in stdin:
    a=int(a)
    c=primo(a)
    if c==True: 
        t="ES PRIMO"
    else:
        t="NO ES PRIMO"
    print(t)