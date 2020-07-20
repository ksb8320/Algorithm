import sys
sys.stdin=open("input.txt")

a,b,c=map(int,input().split())
print(max(b-a,c-b)-1)