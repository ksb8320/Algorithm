import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n=int(input())
    lst=sorted(list(map(int,input().split())))
    print("#{} {}".format(t+1," ".join(map(str,lst))))