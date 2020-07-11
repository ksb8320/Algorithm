import sys
from collections import deque
sys.stdin=open("input.txt")

def bfs():

    while queue:
        s=queue.popleft()
        for i in new[s]:
            if i==99:
                return 1
            else:
                queue.append(i)
    return 0

for t in range(10):
    n,m=map(int,input().split())
    lst=list(map(int,input().split()))
    new=[[] for _ in range(100)]

    queue=deque()
    for i in range(len(lst)):
        if i%2==0:
            new[lst[i]].append(lst[i+1])
    
    queue.append(0)
    print("#{} {}".format(t+1,bfs()))