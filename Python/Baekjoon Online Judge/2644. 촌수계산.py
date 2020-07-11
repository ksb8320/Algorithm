import sys
from collections import deque
sys.stdin=open("input.txt")

def bfs():
    global distance
    while queue:
        distance+=1
        for _ in range(len(queue)):
            s=queue.popleft()
            if s==man2:
                return distance-1
            for i in graph[s]:
                if not visited[i]:
                    visited[i]=1
                    queue.append(i)
    return -1

n=int(input())
man1,man2=map(int,input().split())
m=int(input())
graph=[[]for _ in range(n+1)]
visited=[0]*(n+1)
distance=0
queue=deque()

for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

queue.append(man1)
visited[man1]=1
print(bfs())
