def solution(arr):
    key=arr[0]
    answer = [key]
    for i in range(1,len(arr)):
        if key!=arr[i]:
            answer.append(arr[i])
            key=arr[i]
            
    return answer