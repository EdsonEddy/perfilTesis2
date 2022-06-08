a,r =map(str,input().split())
r=int(r)
nuevo=""
nuevo2=""
lon=int(len(a))
if 1 <=lon and lon <=40:
    if r >=0 and r <=lon:
        r=lon-r
        nuevo=a[r:]
        nuevo2=a[:r]
        print(nuevo+nuevo2)