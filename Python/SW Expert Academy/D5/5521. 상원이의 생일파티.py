import sys
from collections import deque
sys.stdin=open("input.txt")

for t in range(int(input())):
    n,m=map(int,input().split())
    rel=[[]for _ in range(n+1)]
    visited=[0]*(n+1)
    distance=[0]*(n+1)
    queue=deque()
    cnt=0

    for _ in range(m):
        a,b=map(int,input().split())
        rel[a].append(b)
        rel[b].append(a)

    queue.append(1)
    visited[1]=1
    
    while queue:
        key=queue.popleft()
        for i in rel[key]:
            if not visited[i]:
                visited[i]=1
                distance[i]=distance[key]+1
                queue.append(i)

    for i in range(len(distance)):
        if 0<distance[i]<3:
            cnt+=1
    print("#{} {}".format(t+1,cnt))

    
    