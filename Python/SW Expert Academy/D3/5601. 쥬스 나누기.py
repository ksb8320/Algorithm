import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n=int(input())
    lst=[]
    for _ in range(n):
        lst.append("1/{}".format(n))
    print("#{} {}".format(t+1," ".join(lst)))