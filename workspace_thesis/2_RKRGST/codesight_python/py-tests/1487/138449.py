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
    y=primo(a)
    if y==True:
        z="ES PRIMO"
    else:
        z="NO ES PRIMO"
    print(z)
