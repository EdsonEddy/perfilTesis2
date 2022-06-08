import sys
if __name__=='__main__':
    for x in sys.stdin:
   		n, k = x.split(' ')
   		k = int(k)
   		print(len(n),n[k-1])