import sys
sys.stdin=open("input.txt")

test=int(input())
for test in range(test):
    lst=list(map(int,input().split()))
    a=lst[0]
    if a==lst[1]:
        print("#{} {}".format(test+1,lst[2]))
    elif a==lst[2]:
        print("#{} {}".format(test+1,lst[1]))
    elif lst[1]==lst[2]:
        print("#{} {}".format(test+1,lst[0]))