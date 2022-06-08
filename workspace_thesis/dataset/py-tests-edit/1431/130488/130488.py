a,b,c,d=map(int,input().split())
i=3
if (a<=10000)and(b<=1000)and(c,d<=1000):
                                                                       while(i<=a):
                                                                                          x=c+d
                                                                                          c=d 
                                                                                          d=x
                                                                                          i=i+1
                                                                       y=x%b
                                                                       print (y)
