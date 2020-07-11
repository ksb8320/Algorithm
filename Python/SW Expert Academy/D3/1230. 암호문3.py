import sys
sys.stdin=open("input.txt")


for t in range(10):
    n=int(input())
    key=list(map(int,input().split()))
    command_num=int(input())
    command=list(map(str,input().split()))

    for i in range(len(command)):
        if command[i]=="I":
            for j in range(i+3,int(command[i+2])+(i+3)):
                key.insert((int(command[i+1])+(j-i-3)),int(command[j]))
        elif command[i]=="D":
            for k in range(int(command[i+2])):
                key.pop(int(command[i+1]))
        elif command[i]=="A":
            for l in range(i+2,int(command[i+1])+(i+2)):
                key.append(int(command[l]))
    
    print("#{} {}".format(t+1," ".join(map(str,key[0:10]))))