import sys

"""
if __name__ == '__main__':
	for line in sys.stdin:
		while(line !="fin"):
"""
r=input();
while r!="fin":
	m=int(r)
	c=0
	for i in range(m):
		c+=int(input())

	print(c)
	r=input()
		