import sys
sys.stdin=open("input.txt")

def perm(depth,idx,hap):
    global result
    if depth==n:
        hap+=abs(new[idx][0]-home[0])+abs(new[idx][1]-home[1])
        if result>hap:
            result=hap
        return
    elif result<=hap:
        return
    else:
        for i in range(1,len(new)):
            if not visited[i]:
                visited[i]=1
                perm(depth+1,i,hap+abs(new[idx][0]-new[i][0])+abs(new[idx][1]-new[i][1]))
                visited[i]=0

for t in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    visited=[0]*(n+1)
    result=100000
    new=[]

    home=(lst[2],lst[3])
    new.append((lst[0],lst[1]))
    
    for i in range(4,len(lst),2): 
        new.append((lst[i],lst[i+1]))
    perm(0,0,0)
    print("#{} {}".format(t+1,result))