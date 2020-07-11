for test in range(int(input())):
    n=int(input())
    lst=[0,1,1]
    if n>2:
        for i in range(n-2):
            lst.append(lst[i]+lst[i+1])
    lst.pop(lst[0])

    print("#{} {}".format(test+1,lst[n-1]))