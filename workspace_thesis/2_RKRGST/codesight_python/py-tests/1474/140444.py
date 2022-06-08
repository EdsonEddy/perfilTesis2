from sys import stdin, stdout
n = stdin.readline()
n = int(n)
cad1 = stdin.readline()
cad2 = stdin.readline()
v1 = cad1.split(" ")
v2 = cad2.split(" ")
for i in range(n):
    v1[i] = int(v1[i])
    v2[i] = int(v2[i])
for i in range(n):
    x = stdin.readline()
    y = x.split("\n")
    if(y[0] == "+"):
        stdout.write(str(v1[i] + v2[i]) + '\n')
    elif(y[0] == "*"):
        stdout.write(str(v1[i] * v2[i]) + '\n')
    elif(y[0] == ">"):
        stdout.write(str(max(v1[i], v2[i])) + '\n')
    elif(y[0] == "<"):
        stdout.write(str(min(v1[i], v2[i])) + '\n')