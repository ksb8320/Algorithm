from collections import deque
import sys
sys.stdin=open("input.txt")

def dfs(v):
    queue.append(v)
    while queue:
        key=queue.pop()
        for i in graph[key]:
            if not visited[i]:
                visited[i]=1
                lst_a.append(i)
                dfs(i)

n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
queue=deque()
lst_a,lst_b=[],[]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

graph[0].append(0)
for i in range(len(graph)):
    graph[i]=sorted(graph[i])

visited[v]=1
lst_a.append(v)
dfs(v)
print(" ".join(map(str,lst_a)))

visited=[0]*(n+1)
queue.append(v)
visited[v]=1
lst_b.append(v)

while queue:
    key=queue.popleft()
    for i in graph[key]:
        if not visited[i]:
            visited[i]=1
            queue.append(i)
            lst_b.append(i)

print(" ".join(map(str,lst_b)))