def holjak(n):
    string=str(n)
    if int(string[-1])%2==0:
        return "Even"
    else:
        return "Odd"

test=int(input())
for test in range(test):
    n=int(input())
    print("#{} {}".format(test+1,holjak(n)))