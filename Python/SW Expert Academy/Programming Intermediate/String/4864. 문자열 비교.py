import sys
sys.stdin=open("input.txt")

for t in range(int(input())):
    str1=input()
    str2=input()
    if str1 in str2:
        print("#{} {}".format(t+1,1))
    else:
        print("#{} {}".format(t+1,0))
