import sys
sys.stdin=open("input.txt")

def repeat(string):
    stack.append(string[0])

    for i in range(1,len(string)):
        if stack:
            if stack[-1]!=string[i]:
                stack.append(string[i])
            else:
                stack.pop()
        else:
            stack.append(string[i])
    if stack:
        return len(stack)
    else:
        return 0

for t in range(int(input())):
    string=input()
    stack=[]
    print("#{} {}".format(t+1,repeat(string)))