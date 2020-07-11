import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n=int(input())
    arr=[[0 for _ in range(11)] for a in range(11)]
    
    cnt=0
    for i in range(n):
        r1,c1,r2,c2,color=map(int,input().split())
        for x in range(r1,r2+1):
            for y in range(c1,c2+1):
                arr[x][y]+=color
                if arr[x][y]==3:
                    cnt+=1
    
    print("#{} {}".format(t+1,cnt))