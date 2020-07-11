import sys
sys.stdin=open("010101.txt")

test=int(input())
for test in range(test):
    result=sum=0
    arr=list(map(int,input().split()))
    arr.sort()
    arr=arr[1:-1]
    for i in arr:
        sum+=i
    result=round(sum/len(arr))

    print("#{} {}".format(test+1,result))