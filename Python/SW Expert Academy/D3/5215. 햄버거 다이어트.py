import sys
sys.stdin=open("input.txt")

def bread(i,score,calorie):
    global result
    if i==n:
        if calorie<=l:
            if result<score:
                result=score
    else:
        s,c=lst[i]
        bread(i+1,score+s,calorie+c)
        bread(i+1,score,calorie)
        
    return result

for t in range(int(input())):
    n,l=map(int,input().split())
    lst=[]
    result=0
    for _ in range(n):
        lst.append(list(map(int,input().split())))
    
    print("#{} {}".format(t+1,bread(0,0,0)))





# def powerset(arr,visited,n):
#     if n==len(arr):
#         for i in range(len(visited)):
#             if visited[i]==True:
#                 print(arr[i],end=" ")
#         print()
#         return
#     else:
#         visited[n]=True # 지나감
#         powerset(arr,visited,n+1)
#         visited[n]=False # 체크해제
#         powerset(arr,visited,n+1)
# result=[]
# arr=(1,2,3)
# visited=[False]*len(arr)
# print(powerset(arr,visited,0))



