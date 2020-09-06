def solution(prices):
    answer = []
    for i in range(len(prices)):
        key=0
        for j in range(i+1,len(prices)):
            if prices[i]>prices[j]:
                key+=1
                if key==1:
                    answer.append(1)
                else:
                    answer.append(key)
                break
            elif prices[i]<=prices[j]:
                key+=1
        if i+1==len(answer):
            continue
        else:
            answer.append(key)
        
    return answer