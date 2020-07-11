import sys
sys.stdin=open("input.txt")

def dfs(i):
    for j in node[i]:
        if not visited[j]:
            visited[j]=1
            dfs(j)

for t in range(int(input())):
    n,m=map(int,input().split())
    node=[[] for _ in range(n+1)]
    cnt=0
    visited=[0]*(n+1)
    
    for i in range(m):
        a,b=map(int,input().split())
        node[a].append(b)
        node[b].append(a)

    for i in range(1,n+1):
        if not visited[i]:
            visited[i]=1
            cnt+=1
            dfs(i)
    print("#{} {}".format(t+1,cnt))