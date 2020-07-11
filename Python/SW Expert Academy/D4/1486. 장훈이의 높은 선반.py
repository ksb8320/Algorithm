import sys
sys.stdin=open("input.txt")

def check(depth,hap):
    global result
    if depth==n:
        if hap>=b and result>hap:
            result=hap
        return
    elif result<=hap:
        return
    else:
        visited[depth]=1
        check(depth+1,hap+height[depth])
        visited[depth]=0
        check(depth+1,hap)

for t in range(int(input())):
    n,b=map(int,input().split())
    height=list(map(int,input().split()))
    
    visited=[0]*n
    result=1000000
    check(0,0)
    print("#{} {}".format(t+1,result-b))