def solution(s):
    answer = ''
    temp=""
    for i in range(len(s)):
        if s[i]!=" ":
            temp+=s[i]
        elif s[i]==" ":
            for j in range(len(temp)):
                if j%2==0:
                    answer+=temp[j].upper()
                else:
                    answer+=temp[j].lower()
            temp=""
            answer+=" "
    for i in range(len(temp)):
        if i%2==0:
            answer+=temp[i].upper()
        else:
            answer+=temp[i].lower()
    
    return answer