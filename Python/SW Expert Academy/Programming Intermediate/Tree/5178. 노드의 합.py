import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n,m,l=map(int,input().split())
    lst=[0]*(n+2)
    for i in range(m):
        num,value=map(int,input().split())
        lst[num]+=value

    for i in range(m,0,-1):
        if lst[i]==0:
            lst[i]=lst[2*i]+lst[2*i+1]

    print("#{} {}".format(t+1,lst[l]))
    
    
