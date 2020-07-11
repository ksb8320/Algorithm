n=int(input())
arr=[[int(y) for y in input().split()] for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k]==1 and arr[k][j]==1:
                arr[i][j]=1

for i in range(n):
    string=""
    for j in range(n):
        string+=str(arr[i][j])+" "
    print(string)