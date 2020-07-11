import sys
sys.stdin=open("input.txt")

def perm(k,before,s):
    global result
    if k==n:
        s+=arr[before][0]
        if result>s:
            result=s
        return
    elif result<=s:
        return
    else:
        for i in range(1,n):
            if not visited[i]:
                visited[i]=1
                perm(k+1,i,s+arr[before][i])
                visited[i]=0
    return

for t in range(int(input())):
    n=int(input())
    arr=[[int(x)for x in input().split()] for _ in range(n)]
    visited=[0]*n
    result=10000

    perm(1,0,0)
    print("#{} {}".format(t+1,result))