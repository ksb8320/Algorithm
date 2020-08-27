def solution(progresses, speeds):
    answer = []
    day,time=[0]*(len(progresses)),[0]*101
    for i in range(len(progresses)):
        key=progresses[i]
        while key<100:
            key+=speeds[i]
            day[i]+=1
    for i in range(1,len(day)):
        if day[i]<day[i-1]:
            day[i]=day[i-1]
    for i in range(len(day)):
        time[day[i]]+=1
    for i in range(len(time)):
        if time[i]!=0:
            answer.append(time[i])

    return answer