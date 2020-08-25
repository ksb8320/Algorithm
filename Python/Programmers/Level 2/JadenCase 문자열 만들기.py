def solution(s):
    answer=""
    ans=list(s.lower().split(" "))
    for i in range(len(ans)):
        answer+=ans[i].capitalize()+" "
    return answer[:-1]