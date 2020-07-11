import sys
sys.stdin=open("input.txt")

for test in range(int(input())):
    n,m=map(int,input().split())
    lst=list(map(int,input().split()))

    for i in range(m):
        a=lst.pop(0)
        lst.append(a)
    print("#{} {}".format(test+1,lst[0]))