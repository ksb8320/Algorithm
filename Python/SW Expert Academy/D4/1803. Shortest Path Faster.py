import sys
from collections import deque
sys.stdin=open("input.txt")

for t in range(int(input())):
    inf=float('inf')
    n,m,s,e=map(int,input().split())
    graph=[[]for _ in range(n+1)]
    queue=deque()
    dis=[inf]*(n+1)

    for i in range(m):
        a,b,v=map(int,input().split())
        graph[a].append((b,v))
        graph[b].append((a,v))

    queue.append(s)
    dis[s]=0
    
    while queue:
        i=queue.popleft()
        for idx,val in graph[i]:
            if dis[idx]>dis[i]+val:
                dis[idx]=dis[i]+val
                queue.append(idx)
    
    print("#{} {}".format(t+1,dis[e]))
            