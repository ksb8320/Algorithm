def solution(N, stages):
    answer,res=[],[]
    cnt=0
    for i in range(1,N+1):
        key,fail=0,0
        if i in stages:
            key+=stages.count(i)
            fail=key/(len(stages)-cnt)
            cnt+=key
            answer.insert(0,(i,fail))
        elif i not in stages:
            answer.insert(0,(i,0))

    answer=sorted(answer,key=lambda x:x[1])
    for i in range(len(answer)):
        res.insert(0,answer[i][0])

    return res