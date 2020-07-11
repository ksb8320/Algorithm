import sys
sys.stdin=open("input.txt")

for t in range(10):
    n=int(input())
    lst=list(map(int,input().split()))

    cnt=0
    for i in range(2,n-2):
        lmax=max(lst[i-2],lst[i-1])
        rmax=max(lst[i+2],lst[i+1])
        real=max(lmax,rmax)
        if lst[i]>real:
            cnt+=lst[i]-real

    print("#{} {}".format(t+1,cnt))