import sys
sys.stdin=open("input.txt")

def cal(answers,num,n):
    if len(answers)>len(num):
        num=num*((len(answers)//len(num))+1)
    for i in range(len(answers)):       
        if num[i]==answers[i]:
            n+=1
    return n

def solution(answers):
    n1=cal(answers,[1,2,3,4,5],0)
    n2=cal(answers,[2,1,2,3,2,4,2,5],0)
    n3=cal(answers,[3,3,1,1,2,2,4,4,5,5],0)

    lst=[n1,n2,n3]
    key=max(lst)
    answer=[]
    for i in range(3):
        if key==lst[i]:
            answer.append(i+1)
    
    return answer