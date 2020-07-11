import sys
from collections import deque
sys.stdin=open("input.txt")

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def iswall(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    False

for t in range(int(input())):
    n=int(input())
    inf=float('inf')
    arr=[list(map(int,input()))for _ in range(n)]
    distance=[[inf]*n for _ in range(n)]
    queue=deque()

    queue.append((0,0))
    distance[0][0]=0

    while queue:
        x,y=queue.popleft()
        for k in range(4):
            tx=dx[k]+x
            ty=dy[k]+y
            if iswall(tx,ty):
                if distance[tx][ty]>distance[x][y]+arr[tx][ty]:
                    distance[tx][ty]=distance[x][y]+arr[tx][ty]
                    queue.append((tx,ty))
                    
    print("#{} {}".format(t+1,distance[n-1][n-1]))
    
    