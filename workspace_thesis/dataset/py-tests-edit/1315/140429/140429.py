from sys import *#stdin stdout
n=stdin.readline()
v=stdin.readline().split()
stdout.write(str(v[0]))
for i in range(1,len(v)):
	stdout.write(' '+str(int(v[i])-int(v[i-1])))

