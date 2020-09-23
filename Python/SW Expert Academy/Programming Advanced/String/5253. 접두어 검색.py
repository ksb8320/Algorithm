import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n,m=map(int,input().split())
    str_a,str_b,cnt=[],[],0

    for i in range(n+m):
        if i<n:
            str_a.append(input())
        else:
            str_b.append(input())

    for i in range(m):
        for j in range(n):
            if str_b[i]==str_a[j][0:len(str_b[i])]:
                cnt+=1
                break
            
    print("#{} {}".format(t+1,cnt))