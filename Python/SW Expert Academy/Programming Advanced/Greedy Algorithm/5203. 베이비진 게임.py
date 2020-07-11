import sys
sys.stdin=open("input.txt")

def game():
    for i in range(len(card)):
        if i%2==0:
            player1[card[i]]+=1
            for j in range(2,len(player1)):
                if player1[j-2]==3 or player1[j-1]==3 or player1[j]==3 or player1[j-2] and player1[j-1] and player1[j]:
                    return 1
        else:
            player2[card[i]]+=1
            for j in range(2,len(player2)):
                if player2[j-2]==3 or player2[j-1]==3 or player2[j]==3 or player2[j-2] and player2[j-1] and player2[j]:
                    return 2
    return 0

for t in range(int(input())):
    card=list(map(int,input().split()))
    player1,player2=[0]*10,[0]*10
    
    print("#{} {}".format(t+1,game()))

    
    