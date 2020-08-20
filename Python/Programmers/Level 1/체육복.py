def solution(n, lost, reserve):
    lst=[]
    for i in lost:
        for j in reserve:
            if i==j:
                lst.append(i)
                break
            
    for i in range(len(lst)):
        if lst[i] in lost:
            lost.remove(lst[i])
            reserve.remove(lst[i])
    answer = n-len(lost)

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i]-1==reserve[j] or lost[i]+1==reserve[j]:
                answer+=1
                reserve.pop(j)
                break

    return answer