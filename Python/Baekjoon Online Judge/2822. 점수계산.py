import sys
sys.stdin=open("input.txt")

score,lst=[],[]
key=0
for i in range(8):
    score.append((int(input()),i+1))
    
score=sorted(score,key=lambda x:(x[0],x[1]))
score=score[3:]


for i in range(len(score)):
    key+=score[i][0]
    lst.append(score[i][1])
print(key)
print(" ".join(map(str,lst)))
