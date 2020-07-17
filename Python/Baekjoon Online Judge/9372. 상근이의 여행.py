import sys
sys.stdin=open("input.txt")
from collections import deque

for t in range(int(input())):
    n,m=map(int,input().split())
    graph=[[]for _ in range(n+1)]
    vis=[0]*(n+1)
    queue=deque()
    cnt=0

    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    for i in range(len(graph)):
        if graph[i]:
            queue.append(i)
            vis[i]=1
            while queue:
                a=queue.popleft()
                for k in graph[a]:
                    if not vis[k]:
                        vis[k]=1
                        cnt+=1
                        queue.append(k)

    print(cnt)
    
    

    




    
