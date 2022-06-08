import sys
n = int(sys.stdin.readline())
A = [int(i) for i in sys.stdin.readline().split()]
B = [int(i) for i in sys.stdin.readline().split()]
for i in range(n):
	c = sys.stdin.readline();
	if(c[0]=='+'):sys.stdout.write(str(A[i]+B[i])+"\n")
	if(c[0]=='*'):sys.stdout.write(str(A[i]*B[i])+"\n")
	if(c[0]=='>'):sys.stdout.write(str(max(A[i],B[i]))+"\n")
	if(c[0]=='<'):sys.stdout.write(str(min(A[i],B[i]))+"\n")