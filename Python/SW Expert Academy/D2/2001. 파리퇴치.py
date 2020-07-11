import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n,m=map(int,input().split())
    arr=[[int(x) for x in input().split()] for y in range(n)]
    hap=0
    lst=[]
    for i in range(n-m+1):
        for j in range(n-m+1):
            for k in range(i,i+m):
                for l in range(j,j+m):
                    hap+=arr[k][l]
            lst.append(hap)
            hap=0
    print("#{} {}".format(t+1,max(lst)))