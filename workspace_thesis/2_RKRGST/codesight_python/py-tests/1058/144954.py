x=int(input())
for j in range(x):
     n=int(input())
     l=list(map(int,input().split()))
     l=sorted(l)
     for i in l:
	      print(i,end=" ")
     print() 