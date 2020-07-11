import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n,m,l=map(int,input().split())
    lst=list(map(int,input().split()))
    for i in range(m):
        a,b=map(int,input().split())
        lst.insert(a,b)

    print("#{} {}".format(t+1,lst[l]))
