import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n=int(input())
    cnt=0
    lst=[]

    for i in range(n):
        a,b=map(int,input().split())
        lst.append((a,b))
    lst=sorted(lst,key=lambda x:(x[0],x[1]))

    for i in range(n):
        key_a,key_b=lst[i][0],lst[i][1]
        for j in range(i+1,n):
            if lst[j][0]>key_a and lst[j][1]<key_b:
                cnt+=1

    print("#{} {}".format(t+1,cnt))