import sys
sys.stdin=open("input.txt")

for t in range(10):
    n=int(input())
    key=list(map(int,input().split()))
    cmd_cnt=int(input())
    cmd=list(map(str,input().split()))

    for i in range(len(cmd)):
        if cmd[i]=="I":
            for j in range(int(cmd[i+2])):
                key.insert(int(cmd[i+1])+j,int(cmd[i+3+j]))
    print("#{} {}".format(t+1," ".join(map(str,key[0:10]))))