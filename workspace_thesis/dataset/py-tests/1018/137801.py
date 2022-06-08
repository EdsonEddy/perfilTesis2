r=int(input())
for i in range(r):
	a, b= map(int, input().split(" "))
	if(a>b):
		print(">")
	if(a<b):
		print("<")
	if(a==b):
		print("=")



