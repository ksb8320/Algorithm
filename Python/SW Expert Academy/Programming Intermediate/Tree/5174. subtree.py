import sys
sys.stdin=open("input.txt")

def dfs(i):
    global cnt
    if node[i]:
        for j in node[i]:
            cnt+=1
            dfs(j)
    return cnt

for t in range(int(input())):
    e,n=map(int,input().split()) # 간선 e 출발점n
    node=[[]for _ in range(e+2)]
    num=list(map(int,input().split()))
    for i in range(len(num)):
        if i%2==0:
            node[num[i]].append(num[i+1])
    cnt=1
    print("#{} {}".format(t+1,dfs(n)))