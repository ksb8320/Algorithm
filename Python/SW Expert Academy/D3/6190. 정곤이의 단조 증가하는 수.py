import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    new=[]
    res=-1
    for i in range(n):
        for j in range(i+1,n):
            new.append(str(lst[i]*lst[j]))
    for i in new:
        for j in range(1,len(i)):
            if i[j-1]>i[j]:
                break
        else:
            if int(i)>res:
                res=int(i)
    print("#{} {}".format(t+1,res))