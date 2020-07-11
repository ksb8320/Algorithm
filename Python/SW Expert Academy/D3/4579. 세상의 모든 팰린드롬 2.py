import sys
sys.stdin=open("input.txt")

def pal(str):
    for i in range(len(str)):
        if str[i]=="*" or str[-(i+1)]=="*":
            return "Exist"
        elif str[i]!=str[-(i+1)]:
            return "Not exist"
    return "Exist"
test=int(input())
for test in range(test):
    str=input()
    
    print("#{} {}".format(test+1,pal(str)))