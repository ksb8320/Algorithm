import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    str1=list(input())
    str2=list(input())

    lst={}
    for i in str1:
        if not i in lst:
            lst[i]=1
    
    for i in str2:
        if i in lst:
            lst[i]+=1

    print("#{} {}".format(t+1,max(lst.values())-1))

    