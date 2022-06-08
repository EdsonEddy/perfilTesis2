n=int(input())
for i in range (1,n+1,1):
    a, b = map(int, input().split(" "))
    if (a==b):
        print ("=")
    if (a>b) :
        print (">")
    if (a<b) :
        print ("<")
   
