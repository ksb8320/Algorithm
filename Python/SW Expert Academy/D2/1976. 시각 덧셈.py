import sys
sys.stdin=open("010101.txt")

test=int(input())
for test in range(test):
    a,b,c,d=map(int,input().split())
    time=a+c
    min=b+d
    if time>12:
        time=time-12
    if min>=60:
        time+=1
        min=min-60

    print("#{} {} {}".format(test+1,time,min))