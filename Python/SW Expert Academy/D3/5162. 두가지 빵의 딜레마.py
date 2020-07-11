import sys
sys.stdin=open("input.txt")
test=int(input())
for test in range(test):
    a,b,c=map(int,input().split())
    
    print("#{} {}".format(test+1,int(c/min(a,b))))





# v,e=map(int,input().split())
# g=[[]for_ in range(v+1)]

# for _ in range(e):
#     u,v=map(int,input().split())
#     g[u].append(v)
#     g[v].append(u)

# def dfs(v): # v: 현재 방문하는 정점
#     visit[v]=1
#     for w in g[v]:
#         if visit[w]:
#             continue
#         dfs(w)