import sys
sys.stdin=open("input.txt")

dx=[0,1,1,1,0,-1,-1,-1]
dy=[-1,-1,0,1,1,1,0,-1]

def iswall(x,y):
    if 0<=x<h and 0<=y<w:
        return True
    False

def dfs(x,y):
    for k in range(8):
        tx=dx[k]+x
        ty=dy[k]+y
        if iswall(tx,ty) and arr[tx][ty]==1:
            arr[tx][ty]=0
            dfs(tx,ty)

while True:
    w,h=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(h)]
    land=0

    for i in range(h):
        for j in range(w):
            if arr[i][j]==1:
                arr[i][j]=0
                dfs(i,j)
                land+=1
                
    if w==0 and h==0:
        break
    print(land)
