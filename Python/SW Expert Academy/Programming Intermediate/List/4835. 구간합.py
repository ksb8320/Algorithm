import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n,m=map(int,input().split())
    lst=list(map(int,input().split()))
    new=[]
    for i in range(n-m+1):
        result=0
        for j in range(i,i+m):
            result+=lst[j]
        new.append(result)
    print("#{} {}".format(t+1,max(new)-min(new)))

