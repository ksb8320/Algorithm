import sys
sys.stdin=open("input.txt")

for test in range(int(input())):
    a,b=map(int,input().split())

    print("#{} {}".format(test+1,int((a/b)**2)))