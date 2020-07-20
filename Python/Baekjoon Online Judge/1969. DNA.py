import sys
sys.stdin=open("input.txt")

n,m=map(int,input().split())
lst=[list(map(str,input()))for _ in range(n)]
string=""
num=0
for i in range(m):
    cnt=0
    key=""
    a=[['A',0],['C',0],['G',0],['T',0]]
    for j in range(n):
        for k in range(4):
            if lst[j][i]==a[k][0]:
                a[k][1]+=1
    for l in range(len(a)):
        if cnt<a[l][1]:
            cnt=a[l][1]
            key=a[l][0]
    for b in range(len(a)):
        if key!=a[b][0]:
            num+=a[b][1]
    string+=key

print(string)
print(num)
