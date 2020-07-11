import sys
sys.stdin=open("input.txt")

for t in range(10):
    n=int(input())
    lst=list(map(str,input()))
    stack,hap=[],[]

    for i in range(n):
        stack.append(lst[i])
        if len(stack)>2:
            if stack[-2]=="*":
                a=stack.pop(-3)
                b=stack.pop(-1)
                stack.pop()
                stack.append(int(a)*int(b))
    for i in range(len(stack)):
        if stack[i]!="+":
            hap.append(int(stack[i]))

    print("#{} {}".format(t+1,sum(hap)))