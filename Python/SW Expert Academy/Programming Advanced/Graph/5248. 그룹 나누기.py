import sys
sys.stdin=open("input.txt")

def dfs(i):
    global cnt
    for j in graph[i]:
        if not visited[j]:
            visited[j]=1
            dfs(j)

for t in range(int(input())):
    n,m=map(int,input().split())
    lst=list(map(int,input().split()))
    graph=[[] for _ in range(n+1)]
    visited=[0]*(n+1)
    cnt=0

    for i in range(len(lst)):
        if i%2==0:
            graph[lst[i]].append(lst[i+1])
            graph[lst[i+1]].append(lst[i])
    
    for i in range(1,len(graph)):
        if not visited[i]:
            visited[i]=1
            dfs(i)
            cnt+=1
    
    print("#{} {}".format(t+1,cnt))
    
