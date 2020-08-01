import sys
sys.stdin=open("input.txt")

lst=['c=','c-','d-','lj','nj','s=','z=']
alpha=list(input())
cnt=len(alpha)
for i in range(2,len(alpha)+1):
    if alpha[i-2]+alpha[i-1] in lst:
        cnt-=1
    
for i in range(2,len(alpha)):
    if alpha[i-2]+alpha[i-1]+alpha[i]=="dz=":
        cnt-=1
        
print(cnt)
