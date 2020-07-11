import sys
sys.stdin=open("input.txt")

def find(arr,n,key):
    l=0 # 시작
    r=n-1 # 끝
    mid=(l+r)//2
    d=0
    while l<=r:
        if arr[mid]==key:
            return 1
        elif arr[mid]>key:
            if d==1:
                return 0
            r=mid-1
            d=1
        else:
            if d==-1:
                return 0
            l=mid+1
            d=-1
        mid=(l+r)//2
    return 0

for t in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    a.sort() # 안해주면 틀림
    
    cnt=0
    for i in range(m):
        cnt+=find(a,n,b[i])

    print("#{} {}".format(t+1,cnt))