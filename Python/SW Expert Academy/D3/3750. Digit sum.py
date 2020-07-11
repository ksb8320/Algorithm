import sys
sys.stdin=open("input.txt")

new_lst=[]
for test in range(int(input())):
    n=input()
    while len(n)>1:
        lst=[]
        for i in range(len(n)):
            lst.append(int(n[i]))
        n=str(sum(lst))
    new_lst.append(int(n))

for i in range(len(new_lst)):
    print("#{} {}".format(i+1,new_lst[i]))
