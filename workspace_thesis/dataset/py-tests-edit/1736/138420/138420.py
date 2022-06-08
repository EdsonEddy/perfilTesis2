n = int(input())
print(3,end='')
for i in range(1,n):
	print(' ',end='')
	print(((1<<(1<<i))+1),end='')