import sys
sys.stdin=open("010101.txt")

rank=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
test=int(input())
for test in range(test):
    n,k=map(int,input().split()) # 학생수 n, 학점을 알고싶은 학생의 번호k
    lst=[]
    for i in range(n):
        score=list(map(int,input().split()))
        avg=(score[0]*0.35)+(score[1]*0.45)+(score[2]*0.2)
        lst.append(avg)
    lst_a=sorted(lst) # 반대로됨
    lst_b=lst_a[::-1] # 그래서 회문 ㄱ
    result=(lst_b.index(lst[k-1]))//(n//10) # 인덱스함수는 그 값을 호출 가능

    print("#{} {}".format(test+1,rank[result]))