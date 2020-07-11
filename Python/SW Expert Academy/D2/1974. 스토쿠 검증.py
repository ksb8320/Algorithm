import sys
sys.stdin=open("010101.txt")

def stoku():
    lst=[]
    for k in range(0,7,3):
        for l in range(0,7,3):
            lst=[]
            for i in range(k,k+3):
                for j in range(l,l+3):
                    lst.append(arr[i][j])
            if len(set(lst))!=9:
                return 0
    
    for i in range(9):
        lst=[]
        for j in range(9):
            lst.append(arr[i][j])
        if len(set(lst))!=9:
            return 0

    for j in range(9):
        lst=[]
        for i in range(9):
            lst.append(arr[i][j])
        if len(set(lst))!=9:
            return 0
    return 1

test=int(input())
for test in range(test):
    arr=[[int(x) for x in input().split()] for _ in range(9)]

 
    print("#{} {}".format(test+1,stoku()))