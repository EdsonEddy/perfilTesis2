h, m, s = map(int,input().split())
s = s + 1
m = m + (s//60)
s = s % 60
h = h +(m//60)
m = m % 60
h = h % 24
print('{:02d}:{:02d}:{:02d}'.format(h,m,s))