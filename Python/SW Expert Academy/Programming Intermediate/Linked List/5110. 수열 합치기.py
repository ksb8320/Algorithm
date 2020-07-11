import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n,m=map(int,input().split())
    lst=list(map(int,input().split()))
    
    for i in range(m-1):
        a=len(lst)
        new=list(map(int,input().split()))
        for j in range(a):
            if lst[j]>new[0]:
                lst[j:0]=new
                break
        if a==len(lst):
            lst.extend(new)
            
    print("#{} {}".format(t+1," ".join(map(str,lst[-1:-11:-1]))))

    
