import sys
sys.stdin=open("input.txt")

def plus():
    global cnt
    while len(lst)>1:
        new=lst[0]+lst[1]
        if new<10:
            lst.pop(0)
            lst.pop(0)
            lst.insert(0,new)
            cnt+=1
        else:
            lst[0]=1
            lst[1]=new-10
            cnt+=1

    if cnt%2==1:
        return "A"
    else:
        return "B"

for t in range(int(input())):
    num=input()
    lst=[]

    for i in range(len(num)):
        lst.append(int(num[i]))
    cnt=0
    print("#{} {}".format(t+1,plus()))