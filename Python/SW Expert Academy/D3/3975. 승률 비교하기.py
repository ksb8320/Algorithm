import sys
sys.stdin=open("input.txt")

test=int(input())
lst=[]
for test in range(test):
    a,b,c,d=map(int,input().split())
    if a/b>c/d:
        result="ALICE"
    elif a/b<c/d:
        result="BOB"
    else:
        result="DRAW"
    lst.append(result)

for i in range(test+1):
    print("#{} {}".format(i+1,lst[i]))