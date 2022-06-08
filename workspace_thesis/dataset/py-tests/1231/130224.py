a,b,c=map(int,input().split())
seg=a*3600+b*60+c+1
h=seg//3600
if h==24:
	h=0
m=(seg%3600)//60
s=seg%3600%60
print("{:02}:{:02}:{:02}".format(h,m,s))