from sys import stdin
for i in stdin:
    max,num=map(int,i.split())
    min=1
    med=(min+max)//2
    s=1
    while med!=num:
        if med<num:
            min = med + 1
            med=(min+max)//2

            s=s+1
        if med>num:
            max = med - 1
            med=(min+max)//2

            s=s+1
    print(s)