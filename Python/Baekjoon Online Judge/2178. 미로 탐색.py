import sys
sys.stdin=open("input.txt")

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def iswall(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    False

def bfs():
    global result
    while queue:
        x,y=queue.pop(0)
        for k in range(4):
            tx=x+dx[k]
            ty=y+dy[k]
            if iswall(tx,ty)==True and (tx,ty) not in visitied and arr[tx][ty]==1:
                queue.append((tx,ty))
                visitied.append((tx,ty))
                distance[tx][ty]=distance[x][y]+1
                if tx==n-1 and ty==m-1:
                    result=distance[tx][ty]+1
                    return result

n,m=map(int,input().split())
arr=[list(map(int,input()))for _ in range(n)]
distance=[[0 for _ in range(m)]for x in range(n)]
queue=[]
visitied=[]
result=0
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            queue.append((i,j))
            visitied.append((i,j))
            bfs()
print(result)
