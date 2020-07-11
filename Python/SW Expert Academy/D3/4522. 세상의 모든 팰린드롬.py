import sys
sys.stdin=open("input.txt")

def pal(str):
    for i in range(len(str)):
        if str[i]=="?":
            lst.append(str[-(i+1)])
        else:
            lst.append(str[i])
    if lst[::-1]==lst[:]:
        return "Exist"
    return "Not exist"

test=int(input())
for test in range(test):
    str=input()
    lst=[]
    print("#{} {}".format(test+1,pal(str)))