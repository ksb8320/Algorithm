import sys
sys.stdin=open("input.txt")

for test in range(int(input())):
    string=[_ for _ in input()]
    n=len(string)
    new=[0]*n
    
    for i in range(n):
        string[i]=int(string[i])
    cnt=0
    while new!=string:
        for i in range(n):
            if string[i]!=new[i]:
                for j in range(i,n):
                    new[j]=string[i]
                cnt+=1

    print("#{} {}".format(test+1,cnt))
    
    