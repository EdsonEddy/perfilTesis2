n=int(input())
for x in range(n):
	npi,npa=map(int,input().split())
	spi=npi//3
	spa=npa//2
	if spi>spa:
		rs=spa
		rc=(npa%2)+npi-(spa*3)
	else:
		rs=spi
		rc=(npi%3)+npa-(spi*2)
	print(rs,rc)