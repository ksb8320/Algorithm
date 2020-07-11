import sys
sys.stdin=open("input.txt")

def ta(time,target):
    if d==11 and h<11:
        return -1
    elif d==11 and h==11 and m==11:
        return 0
    else:
        return time+target

test=int(input())
for test in range(test): # d=1440h h=1440m m=60
    d,h,m=map(int,input().split())
    target=769
    if d>11:
        time=(d-12)*1440+(h*60)+m
    else:
        time=(h*60)+m-1440
    print("#{} {}".format(test+1,ta(time,target)))