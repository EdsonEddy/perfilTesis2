t=int(input())
if t<=15:
    for k in range(t):
        a, b= map(int, input().split())
        if a>b:
            print (">")
        elif a<b:
            print ("<")
        else:
            print ("=")