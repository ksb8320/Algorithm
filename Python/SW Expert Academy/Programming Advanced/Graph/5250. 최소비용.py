import sys
from collections import deque
sys.stdin=open("input.txt")

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def iswall(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    False

def bfs():
    
    while queue:
        x,y=queue.popleft()
        for k in range(4):
            tx=x+dx[k]
            ty=y+dy[k]
            if iswall(tx,ty):
                cost=1
                if arr[tx][ty]>arr[x][y]:
                    cost+=arr[tx][ty]-arr[x][y]
                if distance[tx][ty]>distance[x][y]+cost:
                    distance[tx][ty]=distance[x][y]+cost
                    queue.append((tx,ty))

    return distance[n-1][n-1]
            
for t in range(int(input())):
    inf=float('inf')
    n=int(input())
    arr=[list(map(int,input().split()))for _ in range(n)]
    distance=[[inf]*n for _ in range(n)]
    queue=deque()
    
    queue.append((0,0))
    distance[0][0]=0
    
    print("#{} {}".format(t+1,bfs()))