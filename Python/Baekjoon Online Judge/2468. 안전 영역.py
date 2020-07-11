import sys
sys.stdin=open("input.txt")
sys.setrecursionlimit(100000)

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def iswall(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    False

def dfs(x,y):
    for k in range(4):
        tx=x+dx[k]
        ty=y+dy[k]
        if iswall(tx,ty)==True and arr[tx][ty]>r and not visited[tx][ty]:
            visited[tx][ty]=1
            dfs(tx,ty)

n=int(input())
arr=[[int(y)for y in input().split()] for _ in range(n)]
result=1

for r in range(1,max(max(arr))):
    visited=[[0]*n for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]>r and visited[i][j]==0:
                visited[i][j]=1
                cnt+=1
                dfs(i,j)

    result=max(result,cnt)
print(result)