import sys
sys.stdin=open("input.txt")

n=int(input())
lst=list(map(int,input().split()))
result=0
new=[]
lst=sorted(lst)
for i in lst:
    result+=i
    new.append(result)
print(sum(new))
