import sys
sys.stdin=open("input.txt")

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def iswall(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    False

def dfs(x,y):
    global result
    for k in range(4):
        tx=x+dx[k]
        ty=y+dy[k]
        if iswall(tx,ty)==True and arr[tx][ty]==0:
            arr[tx][ty]=1
            dfs(tx,ty)
        elif iswall(tx,ty)==True and arr[tx][ty]==3:
            result=1
            return result
    
for t in range(int(input())):
    n=int(input())
    arr=[list(map(int,list(input()))) for _ in range(n)]
    result=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]==2:
                dfs(i,j)
    print("#{} {}".format(t+1,result))
    
    