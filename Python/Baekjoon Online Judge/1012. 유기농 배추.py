import sys
sys.stdin=open("input.txt")

# dx=[1,-1,0,0]
# dy=[0,0,1,-1]

# def iswall(x,y):
#     if x>=0 and y>=0 and x<m and y<n:
#         return True
#     False

# def dfs(x,y):
#     for k in range(4):
#         tx=x+dx[k]
#         ty=y+dy[k]
#         if iswall(tx,ty)==True and arr[tx][ty]==1:
#             arr[tx][ty]=0
#             dfs(tx,ty)

# test=int(input())
# for test in range(test):
#     m,n,k=map(int,input().split()) # m=가로,n=세로,k=배추개수
#     arr=[[0 for y in range(n)] for x in range(m)]
#     cnt=0
    
#     for k in range(k):
#         x,y=map(int,input().split())
#         arr[x][y]=1

#     for i in range(m):
#         for j in range(n):
#             if arr[i][j]==1:
#                 arr[i][j]=0
#                 cnt+=1
#                 dfs(i,j) # 재귀
                
#     print(cnt)

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def iswall(x,y):
    if x<m and y<n and x>=0 and y>=0:
        return True
    False

def dfs(x,y):
    for k in range(4):
        tx=x+dx[k]
        ty=y+dy[k]
        if iswall(tx,ty)==True and arr[tx][ty]==1:
            arr[tx][ty]=0
            dfs(tx,ty)

for test in range(int(input())):
    m,n,k=map(int,input().split())
    arr=[[0 for y in range(n)] for x in range(m)]
    cnt=0

    for a in range(k):
        i,j=map(int,input().split())
        arr[i][j]=1
    
    for i in range(m):
        for j in range(n):
            if arr[i][j]==1:
                arr[i][j]=0
                cnt+=1
                dfs(i,j)
    print(cnt)
        