for test in range(int(input())):
    score=list(map(int,input().split()))
    result=0
    for i in score:
        if i<40:
            i=40
        result+=i
    print("#{} {}".format(test+1,int(result/5)))