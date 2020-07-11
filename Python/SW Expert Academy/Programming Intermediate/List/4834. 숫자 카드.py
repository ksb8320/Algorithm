import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    card=int(input())
    lst=list(map(str,input()))
    cnt=[0]*10
    for i in range(card):
        cnt[int(lst[i])]+=1
    result=0
    for i in range(len(cnt)):
        if result<=cnt[i]:
            result=cnt[i]
            idx=i
    print("#{} {} {}".format(t+1,idx,result))
    