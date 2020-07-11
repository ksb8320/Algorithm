import sys
sys.stdin=open("input.txt")

for t in range(10):
    dump=int(input())
    lst=list(map(int,input().split()))

    while dump>0:
        for i in range(len(lst)):
            if lst[i]==max(lst):
                lst[i]-=1
                break
        for i in range(len(lst)):
            if lst[i]==min(lst):
                lst[i]+=1
                break
        dump-=1
        
    print("#{} {}".format(t+1,max(lst)-min(lst)))