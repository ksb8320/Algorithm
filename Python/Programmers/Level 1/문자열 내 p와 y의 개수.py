def solution(s):
    p_cnt,y_cnt=0,0
    for i in s:
        if i=="p" or i=="P":
            p_cnt+=1
        elif i=="y" or i=="Y":
            y_cnt+=1

    if p_cnt==y_cnt:
        return True
    elif p_cnt!=y_cnt:
        return False