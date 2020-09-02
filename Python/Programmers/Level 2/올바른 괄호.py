def solution(s):
    stack=[s[0]]
    for i in range(1,len(s)):
        if stack:
            k=stack[-1]
            if k=="(" and s[i]=="(":
                stack.append(s[i])
            elif k=="(" and s[i]==")":
                stack.pop()
        else:
            if s[i]=="(":
                stack.append(s[i])
            else:
                return False
    if stack:
        return False

    return True