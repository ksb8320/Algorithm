import sys
sys.stdin=open("input.txt")

def bit(num):
    global n
    if "".join(num[-1:-n-1:-1])=="1"*n:
        return "ON"
    else:
        return "OFF"

for t in range(int(input())):
    n,m=map(int,input().split())
    num=[]
    if m==0:
        num=["0"]
    else:
        while m!=0:
            if m%2==0:
                num.insert(0,"0")
                m//=2
            else:
                num.insert(0,"1")
                m//=2

    print("#{} {}".format(t+1,bit(num)))