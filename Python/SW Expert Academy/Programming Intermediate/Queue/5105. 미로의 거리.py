import sys
sys.stdin=open("input.txt")

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def iswall(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    False

def bfs():
    global result
    while queue:
        x,y=queue.pop(0)
        for k in range(4):
            tx=dx[k]+x
            ty=dy[k]+y
            if iswall(tx,ty) and not visited[tx][ty] and arr[tx][ty]!=1:
                queue.append((tx,ty))
                visited[tx][ty]=visited[x][y]+1
                if arr[tx][ty]==3:
                    result=visited[tx][ty]-1
                    return result

for t in range(int(input())):
    n=int(input())
    arr=[list(map(int,input())) for _ in range(n)]
    queue=[]
    visited=[[0]*n for _ in range(n)]
    result=0

    for i in range(n):
        for j in range(n):
            if arr[i][j]==2:
                queue.append((i,j))
                bfs()
    
    print("#{} {}".format(t+1,result))