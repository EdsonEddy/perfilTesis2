import sys
for line in sys.stdin:
	print('NO' if '00' in line else 'SI')