from sys import stdin, stdout
n = int(input())
if(n < 10):
    stdout.write("hace frio\n")
elif(n > 30):
    stdout.write("hace calor\n")
else:
    stdout.write("esta bien\n")

if(n >= 100):
    stdout.write("hierve\n")
if(n <= 0):
    stdout.write("se congela\n")

