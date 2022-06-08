q,w=1,0
while(q!=w):
        a=int(input())
        if(a==0):
                break
        sumalista = input().split()
        print(eval('+'.join(sumalista)))