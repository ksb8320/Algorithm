import sys
sys.stdin=open("input.txt")

def cal(depth,hap):
    global cnt
    if depth==9:
        if hap==100:
            for i in range(9):
                if vis[i]==1:
                    cnt+=1
            if cnt==7:
                for i in range(9):
                    if vis[i]:
                        new.append(lst[i])
                return
            else:
                cnt=0
    else:
        vis[depth]=1
        cal(depth+1,hap+lst[depth])
        vis[depth]=0
        cal(depth+1,hap)
cnt=0
lst,new=[],[]
vis=[0]*9

for _ in range(9):
    lst.append(int(input()))

cal(0,0)
new=sorted(new)
for i in range(len(new)):
    print(new[i])


