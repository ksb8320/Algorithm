import sys
from collections import deque
sys.stdin=open("input.txt")

n=int(input())
couple=int(input())
node=[[] for _ in range(n+1)]
visited=[0]*(n+1)
queue=deque()
cnt=0

for i in range(couple):
    a,b=map(int,input().split())
    node[a].append(b)
    node[b].append(a)

queue.append(1)
visited[1]=1
while queue:
    key=queue.popleft()
    for i in node[key]:
        if not visited[i]:
            visited[i]=1
            cnt+=1
            queue.append(i)
print(cnt)
