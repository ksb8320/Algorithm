import sys
sys.stdin=open("input.txt")

test=int(input())
for test in range(test):
    n=int(input())
    dic={}
    score=list(map(int,input().split()))
    for i in score:
        if i in dic:
            dic[i]=dic[i]+1
        else:
            dic[i]=1
    max_key=max(dic,key=lambda k: dic[k])
        
    print("#{} {}".format(test+1,max_key))