import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n=int(input())
    lst=[]
    cnt=1
    for _ in range(n):
        lst.append(list(map(int,input().split())))
    lst=sorted(lst,key=lambda x:x[1])
    
    end=lst[0][0]
    for i in range(1,len(lst)):
        if end<=lst[i][0]:
            end=lst[i][1]
            cnt+=1
    print("#{} {}".format(t+1,cnt))

    