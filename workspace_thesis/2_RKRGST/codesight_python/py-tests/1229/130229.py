import math
a,b=map(str,input().split())
if a>b:
	print(f"{a} > {b}")
elif b>a:
	print(f"{a} < {b}")
else:
	print(f"{a} = {b}")	