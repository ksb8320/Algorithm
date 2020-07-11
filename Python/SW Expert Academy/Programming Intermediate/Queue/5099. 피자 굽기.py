import sys
sys.stdin=open("input.txt")

for test in range(int(input())):
    n,m=map(int,input().split())
    lst=list(map(int,input().split()))
    new=[] # 화덕
    number=[]
    num=[]
        
    for i in range(1,m+1):
        num.append(i) # 번호표 빼주는곳
    for j in range(n):
        b=num.pop(0)
        number.append(b)

    for i in range(n):
        a=lst.pop(0)
        new.append(a)

    while len(new)>1:
        new[0]=new[0]//2
        if new[0]==0:
            new.pop(new[0])
            number.pop(0)
            if lst:
                new.append(lst[0])
                lst.pop(0)
                number.append(num[0])
                num.pop(0)
        else:
            first=new.pop(0)
            new.append(first)
            second=number.pop(0)
            number.append(second)
            
    print("#{} {}".format(test+1,number[0]))
