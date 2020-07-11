import sys
sys.stdin=open("input.txt")

def prim():
    key[0]=0
    for _ in range(v+1):
        min_val=inf
        min_idx=-1
        for i in range(v+1):
            if not visited[i] and key[i]<min_val:
                min_idx=i
                min_val=key[i]
        visited[min_idx]=1
        for i,val in graph[min_idx]:
            if not visited[i] and val<key[i]:
                key[i]=val
                parents[i]=min_idx

    return sum(key) # key의 합이 가중치의 합(최소)

for t in range(int(input())):
    inf=float('inf')
    v,e=map(int,input().split())
    graph=[[]for _ in range(v+1)]

    visited=[0]*(v+1)
    key=[inf]*(v+1)
    parents=[0]*(v+1)

    for _ in range(e):
        n1,n2,w=map(int,input().split())
        graph[n1].append((n2,w))
        graph[n2].append((n1,w))

    print("#{} {}".format(t+1,prim()))