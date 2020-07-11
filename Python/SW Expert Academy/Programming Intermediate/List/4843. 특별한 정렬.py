import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n=int(input())
    lst=sorted(list(map(int,input().split())))
    l=len(lst)
    new_a=[]
    new_b=[]
    new=[]
    for i in range(l):
        if i<(l//2):
            new_a.append(lst[i])
        elif i>(l//2)-1:
            new_b.append(lst[i])
    new_b.sort(reverse=True)
    for i in range(5):
        new.append(new_b[i])
        new.append(new_a[i])
    print("#{} {}".format(t+1," ".join(map(str,new))))
