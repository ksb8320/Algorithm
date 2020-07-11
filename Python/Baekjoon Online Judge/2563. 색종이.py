import sys
sys.stdin=open("input.txt")

n=int(input())
arr=[[0]*100 for _ in range(100)]
cnt=0

for _ in range(n):
    x,y=map(int,input().split())
    for i in range(x-1,x+9):
        for j in range(y-1,y+9):
            if not arr[i][j]:
                arr[i][j]=1
                cnt+=1
print(cnt)
