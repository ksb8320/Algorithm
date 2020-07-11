import sys
sys.stdin=open("input.txt")

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def iswall(x,y):
    if 0<=x<16 and 0<=y<16:
        return True
    False

def dfs(x,y):
    global result
    for k in range(4):
        tx=x+dx[k]
        ty=y+dy[k]
        if iswall(tx,ty):
            if arr[tx][ty]==0:
                arr[tx][ty]=1
                dfs(tx,ty)
            elif arr[tx][ty]==3:
                result=1
                return
    
for t in range(10):
    n=int(input())
    arr=[list(map(int,input()))for _ in range(16)]
    result=0
    dfs(1,1)
    print("#{} {}".format(t+1,result))