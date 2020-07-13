import sys
sys.stdin=open("input.txt")
from collections import deque

for t in range(int(input())):
    n,m=map(int,input().split())
    imp=list(map(int,input().split()))
    queue=deque()
    cnt=0

    for i in range(len(imp)):
        queue.append((imp[i],i))

    while queue:
        x,y=queue.popleft()
        if x==max(imp) and y==m:
            cnt+=1
            break
        elif x==max(imp) and y!=m:
            cnt+=1
            imp.remove(x)
        else:
            queue.append((x,y))
            
    print(cnt)