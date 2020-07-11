import sys
sys.stdin=open("input.txt")

n,k=map(int,input().split())
lst=[]
cnt=0
for _ in range(n):
    coin=int(input())
    lst.append(coin)

while k>0:
    if n==1:
        k-=lst[0]
        cnt+=1
    else:
        for i in range(1,n):
            if lst[i-1]<=k<lst[i]:
                k-=lst[i-1]
                cnt+=1
            elif lst[-1]<=k:
                k-=lst[-1]
                cnt+=1
print(cnt)