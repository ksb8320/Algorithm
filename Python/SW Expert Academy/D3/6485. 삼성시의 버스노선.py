import sys
sys.stdin=open("input.txt")

test=int(input())
for test in range(test):
    lst=[0]*5000
    result=[]
    
    n=int(input())
    for i in range(n):
        a,b=map(int,input().split())
        for j in range(a,b+1):
            lst[j-1]+=1

    p=int(input())
    for i in range(p):
        c=int(input())
        result.append(lst[c-1])
    new_result=" ".join(map(str,result))

    print("#{} {}".format(test+1,new_result))