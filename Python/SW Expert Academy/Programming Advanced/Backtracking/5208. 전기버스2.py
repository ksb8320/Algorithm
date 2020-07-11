import sys
sys.stdin=open("input.txt")

def perm(depth,bat,change):
    global result
    if depth==lst[0]:
        if result>change:
            result=change
        return
    elif result<=change:
        return
    else:
        if bat>0:
            perm(depth+1,bat-1,change)
        perm(depth,lst[depth],change+1)
                       
for t in range(int(input())):
    
    lst=list(map(int,input().split()))
    result=10000
    perm(1,lst[1],0)
    print("#{} {}".format(t+1,result))