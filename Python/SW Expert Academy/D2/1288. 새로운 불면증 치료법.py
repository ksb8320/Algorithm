import sys
sys.stdin=open("input.txt")

test=int(input())
for test in range(test):
    n=int(input())
    lst=[]
    new_lst=""
    cnt=0
    while len(lst)<10:
        i=1
        while i>0:
            if n*i<10:
                lst.append(str(n*i))
                cnt+=1
            elif n*i>=10:
                cnt+=1
                for j in range(len(str(n*i))): 
                    new_lst=(str(n*i)[j])
                    if not new_lst in lst:
                        lst.append(new_lst)
            i+=1
            if len(lst)==10:
                break  
    print("#{} {}".format(test+1,cnt*n))