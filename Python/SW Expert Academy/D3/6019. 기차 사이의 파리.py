test=int(input())
for test in range(test):
    d,a,b,f=map(int,input().split())
    time=d/(a+b)
    print("#{} {}".format(test+1,f*time))