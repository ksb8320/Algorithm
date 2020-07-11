import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    n=int(input())
    # 함수 점화식 생성
    result=0
    def fibo(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        return fibo(n-1)+(2*fibo(n-2))

    n=n//10
    result=fibo(n+1)

    print("#{} {}".format(t+1,result))