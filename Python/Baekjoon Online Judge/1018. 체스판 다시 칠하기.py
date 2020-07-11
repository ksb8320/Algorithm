import sys
sys.stdin=open("input.txt")

n,m=map(int,input().split())
arr=[list(map(str,input())) for _ in range(n)]
cnt=0
result=[]

wb=[[0 for _ in range(8)] for _ in range(8)]
bw=[[0 for _ in range(8)] for _ in range(8)]

#wb
for i in range(8):
    for j in range(8):
        if i%2==0 and j%2==0:
            wb[i][j]="W"
        elif i%2==0 and j%2!=0:
            wb[i][j]="B"
        elif i%2!=0 and j%2==0:
            wb[i][j]="B"
        else:
            wb[i][j]="W"

#bw
for i in range(8):
    for j in range(8):
        if i%2==0 and j%2==0:
            bw[i][j]="B"
        elif i%2==0 and j%2!=0:
            bw[i][j]="W"
        elif i%2!=0 and j%2==0:
            bw[i][j]="W"
        else:
            bw[i][j]="B"

for i in range(n-7):
    for j in range(m-7):
        cnt=0
        for x in range(8):
            for y in range(8):
                if arr[x+i][y+j]!=bw[x][y]:
                    cnt+=1
        result.append(cnt)

for i in range(n-7):
    for j in range(m-7):
        cnt=0
        for x in range(8):
            for y in range(8):
                if arr[x+i][y+j]!=wb[x][y]:
                    cnt+=1
        result.append(cnt)
 
print(min(result))

