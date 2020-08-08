def cal(n,arr,new_arr):
    for i in range(n):
        if arr[i]!=0:
            while arr[i]!=1:
                new_arr[i].insert(0,arr[i]%2)
                arr[i]//=2
            new_arr[i].insert(0,arr[i])
            
    for i in range(n):
        if len(new_arr[i])<n:
            for j in range(n-len(new_arr[i])):
                new_arr[i].insert(0,0)
    return new_arr

def solution(n, arr1, arr2):
    new_arr1,new_arr2=[[]for i in range(n)],[[]for i in range(n)]
    answer=[]
    new_arr1=cal(n,arr1,new_arr1)
    new_arr2=cal(n,arr2,new_arr2)
    
    for i in range(n):
        res=""
        for j in range(n):
            new_arr1[i][j]+=new_arr2[i][j]
            if new_arr1[i][j]>0:
                res+="#"
            elif new_arr1[i][j]==0:
                res+=" "
        answer.append(res)

    return answer