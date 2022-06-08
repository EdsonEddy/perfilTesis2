import sys


if __name__ == '__main__':
	for line in sys.stdin:

		c=0
		for i in range(int(line)):
			c+=int(input())

		print(c)
	