def solution(d, budget):
    answer = 0
    while min(d)<=budget:
        if budget>=min(d):
            budget-=min(d)
            answer+=1
            d.pop(d.index(min(d)))
        if not d:
            break
    return answer