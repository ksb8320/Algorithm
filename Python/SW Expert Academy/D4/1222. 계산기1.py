import sys
sys.stdin=open("input.txt")

for t in range(10):
    n=int(input())
    lst=input()
    result=0
    for i in range(n):
        if lst[i]!="+":
            result+=int(lst[i])
    print("#{} {}".format(t+1,result))