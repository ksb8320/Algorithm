import sys
sys.stdin=open("input.txt")

alpha=input()
alphabet=["a","b","c","d","e","f",
        "g","h","i","j","k","l","m",
        "n","o","p","q","r","s","t",
        "u","v","w","x","y","z"]
for i in range(len(alpha)):
    for j in range(len(alphabet)):
        if alpha[i]==alphabet[j]:
            alphabet[j]=i
            break
for i in range(len(alphabet)):
    if type(alphabet[i])==str:
        alphabet[i]=-1
print(" ".join(map(str,alphabet)))

