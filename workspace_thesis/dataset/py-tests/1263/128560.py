import sys

if __name__=='__main__':

    for x in sys.stdin:
    	n, k = map(int, x.split())
    	mid = 0
    	i = 1
    	j = n
    	ans = 0
    	while mid != k:
    		ans += 1
    		mid = (i+j)//2
    		if k>=mid:
    			i = mid + 1
    		else:
    			j = mid - 1
    	print(str(ans)) 