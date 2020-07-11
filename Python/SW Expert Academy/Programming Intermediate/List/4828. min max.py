import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    print("#{} {}".format(t+1,max(lst)-min(lst)))
