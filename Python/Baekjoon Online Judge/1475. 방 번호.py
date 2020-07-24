import sys
sys.stdin=open("input.txt")

num=[0]*10
new=input()
n=[]

for i in range(len(new)):
    if new[i]=='6':
        n.append('9')
    else:
        n.append(new[i])
      
for i in range(len(n)):
    num[int(n[i])]+=1

num[-1]=(num[-1]+1)//2
print(max(num))
