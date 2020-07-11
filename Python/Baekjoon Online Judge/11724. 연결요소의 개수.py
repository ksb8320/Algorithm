import sys
sys.stdin=open("input.txt")

def dfs(i):
    visited[i]=1
    for k in node[i]:
        if not visited[k]:
            dfs(k)

n,m=map(int,input().split())
node=[[] for _ in range(n+1)]
visited=[0]*(n+1)
cnt=0

for _ in range(m):
    u,v=map(int,input().split())
    node[u].append(v)
    node[v].append(u)

for i in range(1,n+1):
    if not visited[i]:
        cnt+=1
        dfs(i)

print(cnt)