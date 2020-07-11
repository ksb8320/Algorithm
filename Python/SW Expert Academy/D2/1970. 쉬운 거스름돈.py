import sys
sys.stdin=open("010101.txt")


test=int(input())
for test in range(test):
    n=int(input())
    a=b=c=d=e=f=g=h=0
    while n>0:
        if n>=50000:
            a=n//50000
            n=n-50000*a
        elif 10000<=n<50000:
            b=n//10000
            n=n-10000*b
        elif 5000<=n<10000:
            c=n//5000
            n=n-5000*c
        elif 1000<=n<5000:
            d=n//1000
            n=n-1000*d
        elif 500<=n<1000:
            e=n//500
            n=n-500*e
        elif 100<=n<500:
            f=n//100
            n=n-100*f
        elif 50<=n<100:
            g=n//50
            n=n-50*g
        elif 10<=n<50:
            h=n//10
            n=n-10*h
        elif 10>n:
            n=0

    print("#{}".format(test+1))
    print("{} {} {} {} {} {} {} {}".format(a,b,c,d,e,f,g,h))