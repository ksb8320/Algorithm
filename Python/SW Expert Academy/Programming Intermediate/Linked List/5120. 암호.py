import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    
    n,m,k=map(int,input().split())
    lst=list(map(int,input().split()))
    key=0
    for i in range(k):
        a=len(lst)
        key+=m
        if key>a:
            key-=a
            
        if key<a:
            lst.insert(key,lst[key-1]+lst[key])
        else:
            lst.append(lst[0]+lst[-1])

    if a<10:
        print("#{} {}".format(t+1," ".join(map(str,lst[::-1]))))
    else:
        print("#{} {}".format(t+1," ".join(map(str,lst[-1:-11:-1]))))