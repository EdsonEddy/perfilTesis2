h,m,s=map(int,input().split())
s+=1
m=m+s//60
h=h+m//60
s%=60
m%=60
h%=24
print(´{:02d}:{:02d}:{:02d}`.format(h,m,s)) 