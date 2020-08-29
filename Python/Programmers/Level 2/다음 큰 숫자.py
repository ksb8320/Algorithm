def solution(n):
    key,cnt,answer,num=n,0,0,[]
    while n>0:
        if n%2==0:
            n//=2
            num.insert(0,0)
        else:
            n//=2
            num.insert(0,1)
            cnt+=1

    for i in range(key+1,1000000):
        k_cnt,k_num=0,i
        while i>0:
            if i%2==0:
                i//=2
            else:
                i//=2
                k_cnt+=1
        if k_cnt==cnt:
            answer=k_num
            break
    
    return answer