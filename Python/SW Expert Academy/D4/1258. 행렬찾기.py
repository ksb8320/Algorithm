import sys
sys.stdin=open("input.txt")

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
        if iswall(tx,ty) and arr[tx][ty]!=0:
            arr[tx][ty]=0
            lst.append((tx,ty))
            dfs(tx,ty)

def cal(lst):
    nx=max(lst)[0]-min(lst)[0]+1
    ny=max(lst)[1]-min(lst)[1]+1
    new.append([nx*ny,nx,ny])
    
    
for t in range(int(input())):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    cnt=0
    lst,new,save=[],[],[]

    for i in range(n):
        for j in range(n):
            if arr[i][j]!=0:
                arr[i][j]=0
                lst.append((i,j))
                dfs(i,j)
                cal(lst)
                lst=[]
                cnt+=1

    
    save.append(cnt)
    new.sort()
    
    for spot in new:
        del spot[0]
        for j in range(2):
            save.append(spot[j])
    
    print("#{} {}".format(t+1," ".join(map(str,save))))
    
    