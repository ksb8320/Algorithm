import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n=int(input())
    lst=[]
    for _ in range(n):
        lst.append(int(input()))
    avg=sum(lst)//n
    cnt=0
    while min(lst)!=avg or max(lst)!=avg:
        for i in range(n):
            if lst[i]>avg:
                lst[i]-=1
                cnt+=1
            elif lst[i]<avg:
                lst[i]+=1
                cnt+=1
    print("#{} {}".format(t+1,cnt//2))
