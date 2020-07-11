import sys
sys.stdin=open("input.txt")

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def iswall(x,y):
    if 0<=x<100 and 0<=y<100:
        return True
    False

for t in range(10):
    n=int(input())
    arr=[list(map(int,input()))for _ in range(100)]
    stack=[]
    result=0
    stack.append((1,1))
    while stack:
        x,y=stack.pop()
        for k in range(4):
            tx=dx[k]+x
            ty=dy[k]+y
            if iswall(tx,ty):
                if arr[tx][ty]==0:
                    arr[tx][ty]=1
                    stack.append((tx,ty))
                elif arr[tx][ty]==3:
                        result=1
                        break
                    
    print("#{} {}".format(t+1,result))

    