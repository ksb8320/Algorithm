# import sys
# sys.stdin=open("input.txt")

test=int(input())
for test in range(test):
    n=int(input())
    avg=0
    arr=[[str(x) for x in input().split()]for _ in range(n)]
    for i in range(n):
        avg+=float(arr[i][0])*int(arr[i][1])
    
    print("#{} {}".format(test+1,"%0.6f"% avg))
