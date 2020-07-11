import sys
sys.stdin=open("input.txt")

def repeat(key,i):
    if i==m:
        return key
    return repeat(key*n,i+1)

for t in range(10):
    num=int(input())
    n,m=map(int,input().split())
    key=n
    print("#{} {}".format(t+1,repeat(key,1)))