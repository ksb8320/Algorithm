import sys
sys.stdin=open("input.txt")

test=int(input())
for test in range(test):
    p,q,r,s,w=map(int,input().split())
    a_fee=b_fee=0

    a_fee=p*w
    if w<=r:
        b_fee=q
    elif w>r:
        b_fee=q+(w-r)*s
    if a_fee<b_fee:
        result=a_fee
    else:
        result=b_fee
    print("#{} {}".format(test+1,result))
    