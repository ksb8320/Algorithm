import sys
sys.stdin=open("input.txt")

alphabet=["a","b","c","d","e","f",
        "g","h","i","j","k","l","m",
        "n","o","p","q","r","s","t",
        "u","v","w","x","y","z"]
n=int(input())
cnt=n
for i in range(n):
    string=input()
    vis=[0]*26
    for j in range(len(string)):
        if string[j] in alphabet:
            vis[alphabet.index(string[j])]+=1
            if vis[alphabet.index(string[j])]>1 and string[j-1]!=string[j]:
                cnt-=1
                break

print(cnt)
