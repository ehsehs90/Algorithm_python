def solution (skill, skill_trees):
    answer = 0
    for str in skill_trees:
        temp = ""
        isOk = True
        for s in str:
            if skill.find(s) != -1:
                temp += s
                print(temp)

        for i in range(len(temp)):
            if skill[i] != temp[i]:
                isOk= False
                print('가자가자')
                break

        if isOk == True:
            answer += 1 

    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
