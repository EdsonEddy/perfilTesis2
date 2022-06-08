s,r = map(str,input().split(' '))
r = int(r)
a = s[len(s)-r:]
b = s[:len(s)-r]
print(a+b)