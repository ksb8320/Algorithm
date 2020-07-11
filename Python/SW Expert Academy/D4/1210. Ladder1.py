import sys
sys.stdin=open("input.txt")

dx=[0,0,-1]
dy=[1,-1,0]

def iswall(x,y):
    if 0<=x<100 and 0<=y<100:
        return True
    False

def dfs(x,y):
    if not x:
        return y
    for k in range(3):
        tx=x+dx[k]
        ty=y+dy[k]
        if iswall(tx,ty) and not visited[tx][ty] and arr[tx][ty]:
            visited[tx][ty]=1
            return dfs(tx,ty)
            
for _ in range(10):
    t=int(input())
    arr=[list(map(int,input().split())) for _ in range(100)]
    visited=[[0]*100 for _ in range(100)]
    result=0
    for j in range(100):
        if arr[99][j]==2:
            visited[99][j]=1
            result=dfs(99,j)
    
    print("#{} {}".format(t,result))