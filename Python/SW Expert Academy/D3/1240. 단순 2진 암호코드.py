import sys
sys.stdin=open("input.txt")

def search(arr):
    new=""
    for i in range(n):
        for j in range(m-1,-1,-1):
            if arr[i][j]=="1":
                for k in range(j,j-57,-1):
                    new+=arr[i][k]
                    if len(new)==7:
                        new_lst.append(new[::-1])
                        new=""
                break
    return new_lst[:8]

def cal(a,b):
    for i in search(arr):
        for j in range(len(lst)):
            if i==lst[j]:
                code.append(lst.index(i))
    
    for i in range(len(code)):
        if i%2!=0:
            a+=code[i]
        else:
            b+=code[i]

    if (a*3+b)%10==0:
        return a+b
    else:
        return 0

for t in range(int(input())):
    n,m=map(int,input().split())
    arr=[[str(x) for x in input()]for _ in range(n)]
    lst=['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
    new_lst=[]
    code=[]

    print("#{} {}".format(t+1,cal(0,0)))   