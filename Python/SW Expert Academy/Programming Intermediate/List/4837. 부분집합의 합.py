import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n,k=map(int,input().split())
    num=[int(i)for i in range(1,13)]
    
    new=[]
    cnt=0
    for i in range(1<<len(num)):
        lst=[]
        for j in range(len(num)):
            if i&(1<<j):
                lst.append(num[j])
        if len(lst)==n and sum(lst)==k:
            cnt+=1
            
    print("#{} {}".format(t+1,cnt))