import sys
sys.stdin=open("input.txt")

n=int(input())
lst=[]
end=cnt=0

for _ in range(n):
    s,e=map(int,input().split())
    lst.append([s,e])
# lst=sorted(lst, key=lambda x:(x[1],x[0])) # 끝나는 시간순으로 정렬
lst=sorted(lst, key=lambda lst:(lst[1],lst[0]))

for i in lst:
    if end<=i[0]:
        end=i[1]
        cnt+=1
print(cnt)
