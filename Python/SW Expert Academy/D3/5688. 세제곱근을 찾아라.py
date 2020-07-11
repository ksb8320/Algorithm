import sys
sys.stdin=open("010101.txt")

test=int(input())
for test in range(test):
    n=int(input())
    result=round(n**(1/3))
    if result**3==n:
        print("#{} {}".format(test+1,result))
    else:
        print("#{} {}".format(test+1,-1))