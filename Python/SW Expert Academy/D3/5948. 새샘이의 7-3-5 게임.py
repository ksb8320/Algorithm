test=int(input())
for test in range(test):
    lst=list(map(int,input().split()))
    new_lst=[]
    result=[]
    visit=[0]*len(lst)

    for i in range(len(lst)):
        if visit[i]==0:
            new_lst.append(lst[i])
            visit[i]=1
        for j in range(i+1,len(lst)):
            if visit[j]==0:
                new_lst.append(lst[j])
                visit[j]=1
            for k in range(j+1,len(lst)):
                if visit[k]==0:
                    new_lst.append(lst[k])
                    visit[k]=1
                    result.append(sum(sorted(new_lst)))
                    new_lst.pop()
                    visit[k]=0

            new_lst.pop()
            visit[j]=0
        new_lst.pop()
        visit[i]=0

    print("#{} {}".format(test+1,list(sorted(set(result)))[-5]))