import sys
sys.stdin=open("input.txt")

def cal():
    global cnt
    for i in range(len(alpha)):
        if alpha[i]==" ":
            cnt+=1
            
alpha=list(map(str,input()))

if alpha[0]!=" " and alpha[-1]!=" ":
    cnt=1
    cal()
elif alpha[0]!=" " and alpha[-1]==" ":
    cnt=0
    cal()
elif alpha[0]==" " and alpha[-1]!=" ":
    cnt=0
    cal()
elif alpha[0]==" " and alpha[-1]==" ":
    cnt=-1
    cal()
print(cnt)
