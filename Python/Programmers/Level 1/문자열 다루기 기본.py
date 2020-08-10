def solution(s):
    num=["0","1","2","3","4","5","6","7","8","9"]
    cnt=0
    if len(s)==4 or len(s)==6:
        for i in range(len(s)):
            if s[i] in num:
                cnt+=1
        if cnt==len(s):
            answer=True
        else:
            answer=False
    else:
        answer=False
    
    return answer