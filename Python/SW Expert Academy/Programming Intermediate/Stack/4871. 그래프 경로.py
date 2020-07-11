import sys
sys.stdin=open("input.txt")

def dfs(s):
    stack.append(s)
    visited[s]=1
    while stack:
        s=stack.pop()
        if s==g:
            return 1
        else:
            for i in route[s]:
                visited[i]=1
                stack.append(i)
    return 0

for t in range(int(input())):
    v,e=map(int,input().split())
    stack=[]
    visited=[0]*(v+1)
    route=[[]*(v+1) for _ in range(v+1)]

    for i in range(e):
        start,end=list(map(int,input().split()))
        route[start].append(end)
    s,g=map(int,input().split())
    
    print("#{} {}".format(t+1,dfs(s)))