import sys
def esPalindrome(n):
	return 1 if n == n[::-1] else 0
for line in sys.stdin:
	c = 0
	for _ in range(int(line)):
		c += esPalindrome(input())
	print(c)