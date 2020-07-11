import sys
sys.stdin=open("input.txt")

n=int(input())

makdae=[64]

while sum(makdae)>n:
    a=min(makdae)//2
    if (sum(makdae)+a)>=n:
        makdae.append(a)
    if a==1:
        break

for i in range(1<<len(makdae)):
    lst=[]
    for j in range(len(makdae)):
        if i&(1<<j):
            lst.append(makdae[j])
    if sum(lst)==n:
        print(len(lst))


        
        