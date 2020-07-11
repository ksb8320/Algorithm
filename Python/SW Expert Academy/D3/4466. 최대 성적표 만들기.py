import sys
sys.stdin=open("input.txt")

test=int(input())
for test in range(test):
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    result=0
    for i in range(k):
        result+=max(lst)
        lst.pop(lst.index(max(lst)))

    print("#{} {}".format(test+1,result))