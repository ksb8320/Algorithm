import sys
sys.stdin=open("input.txt")

n=int(input())
lst,rank=[],[1]*n

for _ in range(n):
    x,y=map(int,input().split())
    lst.append((x,y))

for i in range(n-1):
    for j in range(i+1,n):
        if lst[i][0]<lst[j][0] and lst[i][1]<lst[j][1]:
            rank[i]+=1
        elif lst[i][0]>lst[j][0] and lst[i][1]>lst[j][1]:
            rank[j]+=1

print(" ".join(map(str,rank)))