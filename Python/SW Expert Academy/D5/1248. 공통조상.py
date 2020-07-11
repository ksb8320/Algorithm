import sys
from collections import deque
sys.stdin=open("input.txt")

for t in range(int(input())):
    v,e,num1,num2=map(int,input().split())
    lst=list(map(int,input().split()))
    graph=[[]*(v+1) for _ in range(v+1)]
    
    visited=[0]*(v+1)
    check=[0]*(v+1)
    queue=deque()

    for i in range(e*2):
        if i%2==0:
            graph[lst[i+1]].append(lst[i])
            
    queue.append(num1)
    visited[num1]=1
    queue.append(num2)
    visited[num2]=1
    
    while queue:
        key=queue.popleft()
        for i in graph[key]:
            check[i]+=1
            if not visited[i]:
                visited[i]=1
                queue.append(i)
    
    if 2 in check:
        queue.append(check.index(2))
    new=[check.index(2)]

    graph=[[]*(v+1) for _ in range(v+1)]
    for i in range(e*2):
        if i%2==0:
            graph[lst[i]].append(lst[i+1])
    
    cnt=1
    while queue:
        key=queue.popleft()
        for i in graph[key]:
            queue.append(i)
            cnt+=1
    new.append(cnt)
    print("#{} {}".format(t+1," ".join(map(str,new))))
