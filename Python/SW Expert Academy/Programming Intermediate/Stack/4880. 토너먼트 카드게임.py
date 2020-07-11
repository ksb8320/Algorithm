import sys
sys.stdin=open("input.txt")


def check(start,end): 
    if start==end:
        return start
    else:
        v1=check(start,(start+end)//2)
        v2=check(((start+end)//2)+1,end)

        if num[v1]=="1" and num[v2]=="2":
            return v2
        elif num[v1]=="1" and num[v2]=="3":
            return v1
        elif num[v1]=="2" and num[v2]=="1":
            return v1
        elif num[v1]=="2" and num[v2]=="3":
            return v2
        elif num[v1]=="3" and num[v2]=="1":
            return v2
        elif num[v1]=="3" and num[v2]=="2":
            return v1
        elif num[v1]==num[v2]:
            return v1

for t in range(int(input())):
    n=int(input())
    num=input().split()

    print("#{} {}".format(t+1,check(0,n-1)+1))