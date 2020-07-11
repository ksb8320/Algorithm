import sys
sys.stdin=open("input.txt")

dx=[0,0,1]
dy=[1,-1,0]

def iswall(x,y):
    if 0<=x<100 and 0<=y<100:
        return True
    False

def dfs(x,y):
    global cnt
    for k in range(3):
        tx=x+dx[k]
        ty=y+dy[k]
        if iswall(tx,ty) and not visited[tx][ty] and arr[tx][ty]:
            visited[tx][ty]=1
            cnt+=1
            return dfs(tx,ty)
            
for _ in range(10):
    t=int(input())
    arr=[list(map(int,input().split())) for _ in range(100)]
    distance=[]
    distance_idx=[]
    
    for j in range(100):
        cnt=0
        visited=[[0]*100 for _ in range(100)]
        if arr[0][j]==1:
            visited[0][j]=1
            cnt+=1
            distance_idx.append(j)
            dfs(0,j)
            distance.append(cnt)

    result=distance_idx[distance.index(min(distance))]
    print("#{} {}".format(t,result))