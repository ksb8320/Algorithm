import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    arr=[[str(x) for x in input().split()] for y in range(5)]
    lst=[]
    result=0
    new_result=[]
    
    for i in range(len(arr)):
        if result<len(arr[i][0]):
            result=len(arr[i][0])
    for i in range(5):
        if len(arr[i][0])<result:
            arr[i][0]=arr[i][0]+("-"*(result-len(arr[i][0])))
    for i in range(result):
        for j in range(5):
            if not arr[j][0][i]=="-":
                new_result.append(arr[j][0][i])

    print("#{} {}".format(t+1,"".join(new_result),end=""))