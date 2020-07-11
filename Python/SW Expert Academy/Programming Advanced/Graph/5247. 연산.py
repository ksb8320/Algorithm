from collections import deque
import sys
sys.stdin=open("input.txt")

def cal(num, k):
    if k==0:
        return num+1
    elif k==1:
        return num-1
    elif k==2:
        return num*2
    elif k==3:
        return num-10

def bfs():

    while queue:
        s,cnt=queue.popleft()
        for k in range(4):
            next=cal(s,k)
            if next==m:
                return cnt+1
            if 1<=next<=1000000 and not visited[next]:
                queue.append((next,cnt+1))
                visited[next]=1
                
for t in range(int(input())):
    n,m=map(int,input().split())
    queue=deque()
    visited=[0]*1000001
    cnt=0
    
    queue.append((n,0))
    visited[n]=1
    
    print("#{} {}".format(t+1,bfs()))