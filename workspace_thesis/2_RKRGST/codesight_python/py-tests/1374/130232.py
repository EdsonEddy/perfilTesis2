a,b,c,d=map(int,input().split())
mi,ma=0,0
if a>c:
	mi=a
else:
	mi=c
if b>d:
	ma=d
else:
	ma=b

if mi<=ma:
	print(f"[{mi},{ma}]")
else:
	print("[]")
