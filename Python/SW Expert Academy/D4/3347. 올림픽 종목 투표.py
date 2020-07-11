import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n,m=map(int,input().split()) #조직위원회 m명
    ai=list(map(int,input().split()))
    bi=list(map(int,input().split()))
    # i번째로 있는 종목이 i번째로 재미있는 종목
    # i번 종목을 개최하는 비용 ai
    # j번 위원은 개최비용이 b를 넘지않는 종목중 재미있는경기에 표줌
    lst=[0]*len(ai)
    for i in range(len(bi)):
        for j in range(len(ai)):
            if bi[i]>=ai[j]:
                lst[j]+=1
                break
    print("#{} {}".format(t+1,lst.index(max(lst))+1))
