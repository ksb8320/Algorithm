import sys
sys.stdin=open("input.txt")

n,m=map(int,input().split())
lst_a,lst_b=[],[]

for i in range(n):
    lst_a.append(input())
for i in range(m):
    lst_b.append(input())

res=sorted(set(lst_a)&set(lst_b))
print(len(res))
for i in range(len(res)):
    print(res[i])