import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n,a,b,=map(int,input().split())
    MIN,MAX=0,0
    
    if a+b<=n:
        MIN=min(a,b)
        MAX=0
    elif a+b>n:
        MIN=min(a,b)
        MAX=a+b-n

    print("#{} {} {}".format(t+1,MIN,MAX))