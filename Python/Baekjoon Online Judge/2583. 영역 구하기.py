import sys
sys.setrecursionlimit(1000000)
sys.stdin=open("input.txt")

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def iswall(x,y):
    if x<m and y<n and x>=0 and y>=0:
        return True
    False

def dfs(x,y):
    global cnt
    for k in range(4):
        tx=x+dx[k]
        ty=y+dy[k]
        if iswall(tx,ty)==True and arr[tx][ty]==0:
            arr[tx][ty]=2
            cnt+=1
            dfs(tx,ty)

m,n,k=map(int,input().split())
arr=[[0 for y in range(n)] for x in range(m)]
lst=[]
for a in range(k):
    y1,x1,y2,x2=map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j]=1

for i in range(m):
    for j in range(n):
        if arr[i][j]==0:
            arr[i][j]=2
            cnt=1
            dfs(i,j)
            lst.append(cnt)

print(len(lst))
for i in sorted(lst):
    print(i,end=" ")
