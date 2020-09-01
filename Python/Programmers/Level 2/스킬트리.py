def solution(skill, skill_trees):
    answer = len(skill_trees)
    for i in range(len(skill_trees)):
        lst=[]
        for j in range(len(skill_trees[i])):
            for k in range(len(skill)):
                if skill[k]==skill_trees[i][j]:
                    lst.append(skill[k])
                    break

        for u in range(len(lst)):
            if lst[u]!=skill[u]:
                answer-=1
                break
                
    return answer