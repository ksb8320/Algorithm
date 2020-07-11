import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    string=input()
    result=0   
    for i in range(1,len(string)):
        if string[:i]==string[i:2*i]:
            result=len(string[:i])
            break

    print("#{} {}".format(t+1,result))