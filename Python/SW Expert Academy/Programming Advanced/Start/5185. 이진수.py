import sys
sys.stdin=open("input.txt")

def a(k):
    for i in range(4):
        
        if k&(8>>i):
            print("1",end="")
        else:
            print("0",end="")

for t in range(int(input())):
    n,s=map(str,input().split())
    print("#{}".format(t+1),end=" ")
    for i in range(int(n)):
        t=int(s[i],16)
        a(t)
    #     if s[i]>="0" and s[i]>="9":
    #         a(int(s[i]))
    #     else:
    #         a(ord(s[i])-ord('A')+10)4
    
    print()
    
    
