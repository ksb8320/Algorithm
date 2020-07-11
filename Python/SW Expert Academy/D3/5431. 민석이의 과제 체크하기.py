test=int(input())
for test in range(test):
    n,k=map(int,input().split())
    num=[int(x) for x in input().split()]
    submit=[0]*n
    lst=[]
    for i in range(len(num)):
        submit[(num[i])-1]=1    
    
    for i in range(len(submit)):
        if submit[i]==0:
            lst.append(i+1)
    
    print("#{} {}".format(test+1," ".join(map(str,lst))))