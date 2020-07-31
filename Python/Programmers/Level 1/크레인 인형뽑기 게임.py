import sys
sys.stdin=open("input.txt")

def solution(board, moves):
    lst=[]
    answer=0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]!=0:
                if not lst:
                    lst.append(board[j][i-1])
                    break
                elif lst[-1]==board[j][i-1]:
                    lst.pop()
                    answer+=2
                    break
                else:
                    lst.append(board[j][i-1])
                    break
        board[j][i-1]=0
    return answer