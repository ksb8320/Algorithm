import sys
sys.stdin=open("input.txt")

def check():
    for i in str1:
        if i=="{" or i=="(":
            s.append(i)
        elif i=="}" or i==")":
            if s:
                a=s.pop()
            else:
                return 0
            if a=="{" and i==")":
                return 0
            elif a=="(" and i=="}":
                return 0
    if s:
        return 0
    return 1

for t in range(int(input())):
    str1=input()
    s=[]
    print("#{} {}".format(t+1,check()))
    