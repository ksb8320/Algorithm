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
            
    for i in range(n):
        for j in range(m):
            if str_a[i]==str_b[j]:
                cnt+=1
                break

    print("#{} {}".format(t+1,cnt))