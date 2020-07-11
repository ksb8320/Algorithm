import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n,m=map(int,input().split()) # n: 정점 m: 간선
    node=[[0]*(n+1) for _ in range(n+1)]
    
    for _ in range(m):
        i,j=map(int,input().split())
        node[i][j]=node[j][i]=1
    cnt=0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            for k in range(j+1,n+1):
                if node[i][j] and node[j][k] and node[k][i]:
                    cnt+=1
    print("#{} {}".format(t+1,cnt))
