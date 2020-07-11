import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n,m,l=map(int,input().split())
    lst=list(map(int,input().split()))
    for i in range(m):
        cmd=list(map(str,input().split()))
        if cmd[0]=="I":
            lst.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0]=="D":
            lst.pop(int(cmd[1]))
        else:
            lst[int(cmd[1])]=int(cmd[2])
    if l>=len(lst):
        print("#{} {}".format(t+1,-1))
    else:
        print("#{} {}".format(t+1,lst[l]))
    