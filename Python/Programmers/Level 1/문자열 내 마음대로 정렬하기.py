def solution(strings, n):
    answer=[]
    strings.sort()
    for i in range(len(strings)):
        answer.append([strings[i],strings[i][n]])
    answer=sorted(answer,key=lambda x:x[1])
    
    for i in range(len(answer)):
        answer[i]=answer[i][0]
    
    return answer