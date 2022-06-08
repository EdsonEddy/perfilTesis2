import sys
if __name__=='__main__':
     
    for x in sys.stdin:
        n = int(x)
        print(str(1<<n))