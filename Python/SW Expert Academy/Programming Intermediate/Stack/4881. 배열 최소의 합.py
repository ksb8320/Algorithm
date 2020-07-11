import sys
sys.stdin=open("input.txt")

def perm(depth,idx,hap):
    global result
    if depth==n:
        if result>hap:
            result=hap
        return
    elif result<=hap:
        return
    else:
        for i in range(n):
            if not visit[i]:
                visit[i]=1
                perm(depth+1,i,hap+arr[depth][i])
                visit[i]=0

for t in range(int(input())):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    result=987654321
    visit=[0]*n

    perm(0,0,0)
    print("#{} {}".format(t+1,result))
            
            