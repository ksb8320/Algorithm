import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    card=list(map(str,input()))
    res=[13,13,13,13]
    alpha=["S","D","H","C"]
    cnt=0

    for i in range(0,len(card),3):
        for j in range(i+3,len(card)):
            if card[i:i+3]==card[j:j+3]:
                cnt=1           
        for k in range(4):
            if card[i]==alpha[k]:
                res[k]-=1
    if cnt==0:
        print("#{} {}".format(t+1," ".join(map(str,res))))
    else:
        print("#{} {}".format(t+1,"ERROR"))
