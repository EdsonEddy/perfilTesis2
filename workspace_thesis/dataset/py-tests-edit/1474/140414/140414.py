from sys import *#stdin stdout
n=stdin.readline()
x=stdin.readline().split()
y=stdin.readline().split()
n=int(n)
for i in range(n):
	s=stdin.readline()
	if s[0]=="+":
		stdout.write(str(int(x[i])+int(y[i]))+'\n')
	elif s[0]=="*":
		stdout.write(str(int(x[i])*int(y[i]))+'\n')
	elif s[0]==">":
		stdout.write(str(max(int(x[i]),int(y[i])))+'\n')
	else:
		stdout.write(str(min(int(x[i]),int(y[i])))+'\n')