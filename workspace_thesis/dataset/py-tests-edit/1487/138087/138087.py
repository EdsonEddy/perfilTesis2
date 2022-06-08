from sys import stdin
def primo(n):
    if(n>1):
        c=1
        i=2
        while(i*i<=n):
            if(n%i==0):
                c=0
            i=i+1
        if(c==1):
            print("ES PRIMO")
        else:
            print("NO ES PRIMO")
for n in stdin:
	n=int(n)
	primo(n)
