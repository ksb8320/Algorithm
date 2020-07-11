import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    stick=input()
    cnt=0
    save=[]
    for i in range(len(stick)):
        if stick[i]=="(":
            save.append(1)
        elif stick[i]==")" and stick[i-1]=="(":
            save.pop()
            if save:
                for j in range(len(save)):
                    save[j]+=1
        elif stick[i]==")":
            a=save.pop(-1)
            cnt+=a
    print("#{} {}".format(t+1,cnt))
