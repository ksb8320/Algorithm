import sys
sys.stdin=open("input.txt")

test=int(input())
for test in range(test):
    a_lst=[]
    b_lst=[]
    print("#{}".format(test+1,end=""))
    result=""
    n=int(input())
    for i in range(n):
        alphabet,cnt=map(str,input().split())
        a_lst.append(alphabet)
        b_lst.append(cnt)
    
    for i in range(n):
        result+=a_lst[i]*int(b_lst[i])
    
    for i in range(1,len(result)+1):
        if i%10==0:
            print(result[i-1])
        else:
            print(result[i-1],end="")
    print()