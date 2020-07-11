import sys
sys.stdin=open("input.txt")

test=int(input())
for test in range(test):
    row=input()
    cnt=0
    person=0
    for i in range(len(row)):
        if i>cnt:
            person+=i-cnt
            cnt+=1
        cnt+=int(row[i])
    print("#{} {}".format(test+1,person))