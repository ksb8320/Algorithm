import sys
sys.stdin=open("input.txt")

def bfs():
    global result
    queue.append(s)
    visited[s]=1
    while queue:
        des=queue.pop(0)
        for i in node[des]:
            if not visited[i]:
                visited[i]=1
                queue.append(i)
                distance[i]=distance[des]+1
                if i==g:
                    result=distance[i]
                    return

for t in range(int(input())):
    v,e=map(int,input().split())
    node=[[] for _ in range(v+1)]
    visited=[0]*(v+1)
    distance=[0]*(v+1)
    queue=[]
    result=0

    for _ in range(e):
        n1,n2=map(int,input().split())
        node[n1].append(n2)
        node[n2].append(n1)

    s,g=map(int,input().split())

    bfs()
    print("#{} {}".format(t+1,result))