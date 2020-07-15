import sys
sys.stdin=open("input.txt")

lst=[]
n=int(input())

if n==1:
    print(1)
else:
    for i in range(1,10000):
        if 2**(i-1)<=n<=2**i:
            for j in range(2**(i-1)+1,n+1):
                lst.append(j)
            break

    for i in range(len(lst)):
        if lst[i]==n:
            print((i+1)*2)