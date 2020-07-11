import sys
sys.stdin=open("input.txt")

def prim():
    key[0]=0
    for _ in range(n):
        min_idx=-1
        min_val=inf
        for i in range(n):
            if not visited[i] and key[i]<min_val:
                min_val=key[i]
                min_idx=i
        visited[min_idx]=1
        for i,val in graph[min_idx]:
            if not visited[i] and key[i]>val:
                key[i]=val

    return round(sum(key))

for t in range(int(input())):
    n=int(input())
    inf=float('inf')
    graph=[[] for _ in range(n)]
    visited=[0]*n
    key=[inf]*n
    
    arr_x,arr_y=[],[]

    arr_x=list(map(int,input().split()))
    arr_y=list(map(int,input().split()))
    e=float(input())

    for i in range(n):
        for j in range(n):
            if i!=j:
                graph[i].append((j,e*((arr_x[i]-arr_x[j])**2)+e*(arr_y[i]-arr_y[j])**2))

    print("#{} {}".format(t+1,prim()))