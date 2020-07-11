import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n,m=map(int,input().split())
    twin=n-m
    uni=m-twin
    print("#{} {} {}".format(t+1,uni,twin))
