import sys
sys.stdin=open("input.txt")

test=int(input())
for test in range(test):
    string=input()
    l=len(string)
    h=int(input()) # 몇개의 하이픈 넣으지
    lst=list(map(int,input().split()))
    new_lst=[0]*(len(string)+1)
    a_lst=[]

    for i in range(len(lst)):
        new_lst[lst[i]]+=1

    for i in range(l):
        a_lst.append((new_lst[i])*'-'+string[i])
    a_lst.append(new_lst[-1]*"-")
    print("#{} {}".format(test+1,"".join(a_lst)))