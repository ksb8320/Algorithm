import sys
sys.stdin=open("input.txt")

alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
che="!?."

for t in range(int(input())):
    n=int(input())
    string=input().split(" ")
    n_cnt=[0]*n
    cnt,k=0,0

    for i in range(len(string)):
        for j in range(len(string[i])):
            if string[i][j] in alpha:
                cnt+=1
            elif string[i][j] in num:
                cnt=0
                break
        if cnt==1:
            n_cnt[k]+=1
            cnt=0
        if string[i][-1] in che:
            k+=1

    print("#{} {}".format(t+1," ".join(map(str,n_cnt))))
