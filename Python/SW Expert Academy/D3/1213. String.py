import sys
sys.stdin=open("input.txt")

for t in range(10):
    n=int(input())
    find=input()
    string=input()
    new=0
    for i in range(len(string)-len(find)+1):
        cnt=0
        for j in range(len(find)):
            if string[i+j]==find[j]:
                cnt+=1
        if cnt==len(find):
            new+=1
    print("#{} {}".format(t+1,new))

    # for i in range(len(string)-len(find)+1):
    #     if find[:]==string[i:i+len(find)]:
    #         new+=1
    # print("#{} {}".format(t+1,new))

    