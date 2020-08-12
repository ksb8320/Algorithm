def solution(s, n):
    answer=""
    s_alpha="abcdefghijklmnopqrstuvwxyz"
    b_alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in s:
        if i in s_alpha:
            if n+s_alpha.index(i)>25:
                answer+=s_alpha[n-(26-s_alpha.index(i))]
            else:
                answer+=s_alpha[s_alpha.index(i)+n]
                
        elif i in b_alpha:
            if n+b_alpha.index(i)>25:
                answer+=b_alpha[n-(26-b_alpha.index(i))]
            else:
                answer+=b_alpha[b_alpha.index(i)+n]
        else:
            answer+=i
            
    return answer