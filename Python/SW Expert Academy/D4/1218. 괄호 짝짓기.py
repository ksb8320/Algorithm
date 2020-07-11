import sys
sys.stdin=open("input.txt")

def jjak(lst):
    a1_cnt=a2_cnt=b1_cnt=b2_cnt=c1_cnt=c2_cnt=d1_cnt=d2_cnt=0
    for i in range(len(lst)):
        if lst[i]=="(":
            a1_cnt+=1
        elif lst[i]=="[":
            b1_cnt+=1
        elif lst[i]=="{":
            c1_cnt+=1
        elif lst[i]=="<":
            d1_cnt+=1
        if lst[i]==")":
            a2_cnt+=1
        elif lst[i]=="]":
            b2_cnt+=1
        elif lst[i]=="}":
            c2_cnt+=1
        elif lst[i]==">":
            d2_cnt+=1
    if a1_cnt==a2_cnt and b1_cnt==b2_cnt and c1_cnt==c2_cnt and d1_cnt==d2_cnt:
        return 1
    elif a1_cnt!=a2_cnt or b1_cnt!=b2_cnt or c1_cnt!=c2_cnt or d1_cnt!=d2_cnt:
        return 0

for t in range(10):
    n=int(input())
    
    lst=input()
    print("#{} {}".format(t+1,jjak(lst)))
