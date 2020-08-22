def solution(x):
    x=str(x)
    num=0
    for i in range(len(x)):
        num+=int(x[i])
    if int(x)%num==0:
        return True
    else:
        return False