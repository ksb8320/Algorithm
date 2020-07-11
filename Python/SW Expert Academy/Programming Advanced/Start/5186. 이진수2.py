import sys
sys.stdin=open("input.txt")

def ejinsu(num):
    
    while num!=0:
        if num*2>=1:
            num=num*2-1
            jinsu.append(1)
        else:
            num*=2
            jinsu.append(0)

    if len(jinsu)>=13:
        return "overflow"
    else:
        return "".join(map(str,jinsu))

for t in range(int(input())):
    num=float(input())
    jinsu=[]
    
    print("#{} {}".format(t+1,ejinsu(num)))