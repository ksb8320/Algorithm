# import sys
# sys.stdin=open("input.txt")

n=int(input())
lst=[]
cnt=0
for i in range(1,n+1):
    if i<10 and i%3!=0:
        lst.append(str(i))
    elif i<10 and i%3==0:
        i="-"
        lst.append(str(i))
    elif i>=10:
        for j in range(len(str(i))):
            if int(str(i)[j])%3!=0 or int(str(i)[j])==0:
                cnt+=1
        if cnt==len(str(i)):
            lst.append(str(i))
        cnt=0
        for j in range(len(str(i))):
            if int(str(i)[j])!=0 and int(str(i)[j])%3==0:
                cnt+=1
        sam="-"*cnt
        if len(sam)>=1:
            lst.append(sam)
        cnt=0

print(" ".join(lst))
