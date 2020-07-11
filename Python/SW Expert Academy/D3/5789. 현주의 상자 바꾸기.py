import sys
sys.stdin=open("010101.txt")

test=int(input())
for test in range(test):
    lst=[]
    n,q=map(int,input().split()) #n개의 상자, q회
    sangja=[0]*n

    for i in range(1,q+1):
        l,r=map(int,input().split())
        for j in range(l-1,r):
            sangja[j]=i
    print("#{} {}".format(test+1," ".join(map(str,sangja))))