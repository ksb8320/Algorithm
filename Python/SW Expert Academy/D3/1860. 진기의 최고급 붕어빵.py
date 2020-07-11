import sys
sys.stdin=open("input.txt")

def bread():
    global cnt
    for i in lst:
        for j in range(i):
            if new[j]>0:
                new[j]-=1
                cnt+=1
                break
    if cnt==len(lst):
        return "Possible"
    else:
        return "Impossible"

for test in range(int(input())):
    n,m,k=map(int,input().split()) # n:사람 m:시간 k:만듬
    lst=list(map(int,input().split())) # 언제 도착하는지
    lst=sorted(lst)
    new=[0]*max(lst)
    cnt=0
    for i in range(m-1,max(lst),m):
        new[i]=k

    print("#{} {}".format(test+1,bread()))