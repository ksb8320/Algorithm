import sys
sys.stdin=open("input.txt")

def page(i):
    l=1; r=p
    global cnt
    while 1:
        mid=int((l+r)/2)
        if mid==i:
            return
        if mid<i: 
            l=mid
            cnt+=1
        elif mid>i:
            r=mid
            cnt+=1

for t in range(int(input())):
    p,a,b=map(int,input().split())
    cnt=0
    page(a)
    cnt_a=cnt
    cnt=0
    page(b)
    cnt_b=cnt
    if cnt_a<cnt_b:
        print("#{} {}".format(t+1,"A"))
    elif cnt_a>cnt_b:
        print("#{} {}".format(t+1,"B"))
    else:
        print("#{} {}".format(t+1,0))