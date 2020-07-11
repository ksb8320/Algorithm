import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n=int(input())
    lst=[]
    for i in range(n):
        lst.append(input())

    lst=sorted(set(lst))
    lst=sorted(lst,key=len)
    print("#{}".format(t+1))
    for i in lst:
        print(i)