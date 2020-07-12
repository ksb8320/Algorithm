import sys
sys.stdin=open("input.txt")
from collections import deque

# BFS
for t in range(int(input())):
    inf=float('inf')
    n,m=map(int,input().split())
    graph=[[]for _ in range(n+1)]
    dis=[inf]*(n+1)
    queue=deque()

    for _ in range(m):
        s,e,w=map(int,input().split())
        graph[s].append((e,w))
        
    queue.append(0)
    dis[0]=0
    
    while queue:
        k=queue.popleft()
        for i,val in graph[k]:
            if dis[i]>dis[k]+val:
                dis[i]=dis[k]+val
                queue.append(i)
                
    print("#{} {}".format(t+1,dis[n]))


# 프림 알고리즘
# def prim():
#     key[0]=0
#     for _ in range(n+1):
#         min_val=inf
#         min_idx=-1
#         for i in range(n+1):
#             if not visited[i] and key[i]<min_val:
#                 min_val=key[i]
#                 min_idx=i
#         visited[min_idx]=1
#         for i,val in graph[min_idx]:
#             if key[i]>min_val+val:
#                 key[i]=min_val+val
#     return key[n]

# for t in range(int(input())):
#     n,e=map(int,input().split())
#     inf=float('inf')
#     key=[inf]*(n+1)
#     graph=[[] for _ in range(n+1)]
#     visited=[0]*(n+1)

#     for i in range(e):
#         start,end,w=map(int,input().split())
#         graph[start].append((end,w))

#     print("#{} {}".format(t+1,prim()))