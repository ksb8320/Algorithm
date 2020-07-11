import sys
sys.stdin=open("input.txt")

mo="aeiou"
test=int(input())
for test in range(test):
    string=input()
    lst=[]
    for i in range(len(string)):
        if string[i] in mo:
            continue
        else:
            lst.append(string[i])
    print("#{} {}".format(test+1,"".join(lst)))