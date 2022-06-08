import sys
  
if __name__=='__main__':
    for x in sys.stdin:
        n = int(x)
        v =[0]*500;
        A = [ int (y) for y in input().split()]
        while n:
        	n -= 1        	
        	v[A[n]] = 1
        i = 0
        ans = 0
        while i<500:
        	if v[i]==1:
        		ans += 1
        		i += 1
        	i+=1
        print(str(ans))