import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n,cnt,lst=int(input()),0,list(map(int,input().split()))
    for i in range(len(lst)):
        if lst[i]<=sum(lst)//len(lst):
            cnt+=1
    print("#{} {}".format(t+1,cnt))