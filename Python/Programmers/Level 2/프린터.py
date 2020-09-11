from collections import deque

def solution(priorities, location):
    answer = 0
    queue=deque()
    for i in range(len(priorities)):
        queue.append([priorities[i],i])
    while queue:
        x,y=queue.popleft()
        if x==max(priorities) and y==location:
            answer+=1
            break
        elif x==max(priorities) and y!=location:
            answer+=1
            priorities.remove(x)
        else:
            queue.append((x,y))
    return answer