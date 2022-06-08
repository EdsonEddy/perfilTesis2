n=int(input())
array=input().split()
newarray=array[::-1]
if array==array[::-1]:
    print("SI")
else:
    print("NO")