import sys
sys.stdin=open("input.txt")

for test in range(int(input())):
    n=int(input())
    arr=[[x for x in input()] for a in range(n)]
    result=0
    k=n//2
    for i in range(n):
        if i<=k:
            for j in range(k-i,k+i+1):
                result+=int(arr[i][j])
        else:
            for h in range(i-k,n-i+k):
                result+=int(arr[i][h])
    
    print("#{} {}".format(test+1,result))
    