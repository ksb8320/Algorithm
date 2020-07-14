import sys
sys.stdin=open("input.txt")
from collections import deque

inf=float('inf')
n,m=map(int,input().split())
graph=[[]for _ in range(n+1)]
queue=deque()
lst=[]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    dis,vis=[inf]*(n+1),[0]*(n+1)
    queue.append(i)
    dis[i]=0
    vis[i]=1
    while queue:
        a=queue.popleft()
        for k in graph[a]:
            if not vis[k]:
                vis[k]=1
                if dis[k]>dis[a]+1:
                    dis[k]=dis[a]+1
                    queue.append(k)
    lst.append(sum(dis[1:]))
    
print(lst.index((min(lst)))+1)

