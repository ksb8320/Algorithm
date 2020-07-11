import sys
sys.stdin=open("input.txt")

def perm(depth):
    if depth==m:
        for i in range(m):
            print(lst[i], end=" ")
        print()
    else:
        for i in range(n):
            if not visited[i]:
                visited[i]=1
                lst[depth]=i+1
                perm(depth+1)
                visited[i]=0

n,m=map(int,input().split())

lst=[0]*n
visited=[0]*n
perm(0)