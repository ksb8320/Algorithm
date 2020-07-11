import sys
sys.stdin=open("input.txt")

# dx=[1,-1,0,0]
# dy=[0,0,1,-1]

# def iswall(x,y):
#     if x>=0 and y>=0 and x<n and y<n:
#         return True
#     False

# def dfs(x,y):
#     global cnt

#     for k in range(4):
#         tx=x+dx[k]
#         ty=y+dy[k]
#         if iswall(tx,ty)==True and arr[tx][ty]==1:
#             cnt+=1 # 카운트 세줌
#             arr[tx][ty]=2 # 지나간 경로는 2로 바꿔줌
#             dfs(tx,ty) # 이게 뭔지 궁금
#     else:
#         return cnt

# n=int(input())
# arr=[[int(i) for i in input()] for _ in range(n)]
# cnt=0
# lst=[]
# for i in range(n):
#     for j in range(n):
#         if arr[i][j]==1: # 시작점 찾기
#             arr[i][j]=2
#             cnt=1
#             dfs(i,j) # 시작
#             if cnt!=0:
#                 lst.append(cnt)
# print(len(lst))
# lst.sort()
# for i in range(len(lst)):
#     print(lst[i])

# 14889 14501 14502 15686 165234 14888 17070 17135 15683 17471

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def iswall(x,y):
    if x>=0 and y>=0 and x<n and y<n:
        return True
    False
def dfs(x,y):
    global cnt
    for k in range(4):
        tx=x+dx[k]
        ty=y+dy[k]
        if iswall(tx,ty)==True and arr[tx][ty]==1:
            arr[tx][ty]=2
            cnt+=1
            dfs(tx,ty)
    else:
        return cnt

n=int(input())
arr=[[int(x) for x in input()] for y in range(n)]
lst=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            arr[i][j]=2
            cnt=1
            dfs(i,j)
            if cnt!=0:
                lst.append(cnt)
print(len(lst))
lst.sort()
for i in range(len(lst)):
    print(lst[i])