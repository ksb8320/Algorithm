import sys
sys.stdin=open("input.txt")

for test in range(int(input())):
    n=int(input())
    s1=s2=s3=0
    s1=n*(n+1)//2
    s2=n**2
    s3=2*n*(2*n+1)//2-s2
    print("#{} {} {} {}".format(test+1,s1,s2,s3))