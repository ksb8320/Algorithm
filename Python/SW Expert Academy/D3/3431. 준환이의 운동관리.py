import sys
sys.stdin=open("input.txt")

for test in range(int(input())):
    l,u,x=map(int,input().split())
    if l>x:
        print("#{} {}".format(test+1,(l-x)))
    elif l<x and x<u:
        print("#{} {}".format(test+1,0))
    elif x>u:
        print("#{} {}".format(test+1,-1))