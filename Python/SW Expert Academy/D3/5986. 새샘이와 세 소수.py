def sosu():
    for i in range(2,n):
        cnt=0
        for j in range(1,i+1):
            if i%j==0:
                cnt+=1
        if cnt==2:
            lst.append(j)

test=int(input())
for test in range(test):
    lst=[]
    n=int(input())
    sosu()

    a=len(lst)

    new_cnt=0
    for i in range(a):
        for j in range(i,a):
            if lst[i]+lst[j]>n:
                break
            for k in range(j,a):
                if lst[i]+lst[j]+lst[k]>n:
                    break
                if lst[i]+lst[j]+lst[k]==n:
                    new_cnt+=1
    
    print("#{} {}".format(test+1,new_cnt))

# hap=set(map(tuple,neo_lst))  # 2차원 배열 중복 제거 위해 tuple 사용하기
