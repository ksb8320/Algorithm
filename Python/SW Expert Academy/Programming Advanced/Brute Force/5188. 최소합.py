import sys
sys.stdin=open("input.txt")

dx=[1,0]
dy=[0,1]

def iswall(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    False

def dfs(x,y,hap):
    global result
    if x==n-1 and y==n-1:
        if result>hap:
            result=hap
        return
    elif result<=hap:
        return
    else:
        for k in range(2):
            tx=x+dx[k]
            ty=y+dy[k]
            if iswall(tx,ty)==True:
                dfs(tx,ty,hap+arr[tx][ty])

for t in range(int(input())):
    n=int(input())
    arr=[list(map(int,input().split()))for _ in range(n)]
    result=100000

    dfs(0,0,arr[0][0])
    print("#{} {}".format(t+1,result))