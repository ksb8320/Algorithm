import sys
sys.stdin=open("input.txt")

string=input()
lst=[]

for i in range(len(string)):
    lst.append(string[i:])
lst=sorted(lst)
for i in range(len(lst)):
    print(lst[i])
