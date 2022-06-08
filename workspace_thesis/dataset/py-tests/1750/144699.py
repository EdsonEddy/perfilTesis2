import sys


if __name__ == '__main__':
	for line in sys.stdin:
		line= line.rstrip()
		b= line[::-1]
		c1=''
		c2=''
		sw=False
		for i in range(len(b) // 2+1):
			c1+=line[i]
			c2=b[i]+c2
			if c1==c2:
				sw=True
				break
		if sw:
			print('si')

		else :
			print('no')