import sys
sys.stdin=open("input.txt")

test=int(input())
for test in range(test):
    n=int(input())
    lst=[0]*5
    cnt=0
    while n>1:
        if n%2==0:
            lst[0]+=1
            n=n//2
        if n%3==0:
            lst[1]+=1
            n=n//3
        if n%5==0:
            lst[2]+=1
            n=n//5
        if n%7==0:
            lst[3]+=1
            n=n//7
        if n%11==0:
            lst[4]+=1
            n=n//11
    
    print("#{} {}".format(test+1," ".join(map(str,lst))))
