import sys
sys.stdin=open("input.txt")

for t in range(10):
    n=int(input())
    arr=[[int(x)for x in input().split()]for _ in range(100)]
    result=[]
    
    for i in range(100):
        cnt_g=cnt_s=cnt_d=0
        for j in range(100):
            cnt_g+=arr[i][j]
            cnt_s+=arr[j][i]
            if i==j:
                cnt_d+=arr[i][j]
        result.append(cnt_g)
        result.append(cnt_s)
    result.append(cnt_d)

    for i in range(100):
        for j in range(99,-1,-1):
            if i+j==99:
                cnt_d+=arr[i][j]
    result.append(cnt_d)
    print("#{} {}".format(t+1,max(result)))
    