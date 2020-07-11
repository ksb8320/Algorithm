import sys
sys.stdin=open("input.txt")

test=int(input())
for test in range(test):
    lst=[]
    n=int(input())
    while len(lst)<n:
        lst+=list(map(str,input().split()))

    new="".join(lst)

    for i in range(1000):
        if str(i) not in new:
            print("#{} {}".format(test+1,i))
            break