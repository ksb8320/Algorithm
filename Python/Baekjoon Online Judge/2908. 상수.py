import sys
sys.stdin=open("input.txt")

a,b=map(str,input().split())
a=a[::-1]
b=b[::-1]
if a>b:
    print(a)
elif a<b:
    print(b)
