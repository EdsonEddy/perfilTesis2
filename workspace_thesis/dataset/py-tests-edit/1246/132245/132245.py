import sys
 
if __name__=='__main__':
    for x in sys.stdin:
        s = input()
        n = len(s)
        c = 0
        for i in range(n):
            if s[i]==x[0]:c += 1
        print(str(c))