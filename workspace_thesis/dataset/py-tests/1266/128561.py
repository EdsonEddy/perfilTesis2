import sys
if __name__=='__main__':
    for x in sys.stdin:
    	n, k = map(int, x.split())
    	A = [int (i) for i in input().split()]
    	ans = 0.0
    	for i in range(n):
    		ans += A[i]*(k**(n-1-i))
    	print("{:.1f}".format(ans))