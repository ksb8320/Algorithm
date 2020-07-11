import sys
sys.stdin=open("input.txt")

test=int(input())
for test in range(test):
    n=int(input())
    lst=list(map(str,input().split()))
    new_lst=[]
    a=len(lst)//2

    if len(lst)%2==0:
        lst_a=lst[:a]
        lst_b=lst[a:]
        for i in range(a):
            new_lst.append(lst_a[i])
            new_lst.append(lst_b[i])
    else:
        lst_a=lst[:a+1]
        lst_b=lst[a+1:]
        for i in range(a):
            new_lst.append(lst_a[i])
            new_lst.append(lst_b[i])
        new_lst.append(lst_a[-1])

    print("#{} {}".format(test+1," ".join(new_lst)))