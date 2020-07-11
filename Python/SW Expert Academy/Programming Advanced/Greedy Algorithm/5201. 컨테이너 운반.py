import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n,m=map(int,input().split())
    weight=list(map(int,input().split()))
    ti=list(map(int,input().split()))

    weight=sorted(weight,reverse=True)
    ti=sorted(ti,reverse=True)
    a=0
    for i in weight:
        for j in ti:
            if i<=j:
                a+=i
                ti.pop(ti.index(j))
                break
    print("#{} {}".format(t+1,a))
