import sys
sys.stdin=open("input.txt")

def forth(string):
    for i in range(len(string)):
        if string[i]=="+":
            if len(stack)<2:
                return "error"
            a=stack.pop()
            b=stack.pop()
            stack.append(a+b)
        elif string[i]=="-":
            if len(stack)<2:
                return "error"
            a=stack.pop()
            b=stack.pop()
            if a>b:
                stack.append(a-b)
            elif a<b:
                stack.append(b-a)
        elif string[i]=="*":
            if len(stack)<2:
                return "error"
            a=stack.pop()
            b=stack.pop()
            stack.append(a*b)
        elif string[i]=="/":
            if len(stack)<2:
                return "error"
            a=stack.pop()
            b=stack.pop()
            if a>b:
                stack.append(a//b)
            elif a<b:
                stack.append(b//a)
        elif string[i]==".":
            if len(stack)>1:
                return "error"
            result=stack.pop()
            return result
        else:
            stack.append(int(string[i]))

for t in range(int(input())):
    string=list(map(str,input().split()))
    stack=[]
    
    print("#{} {}".format(t+1,forth(string)))