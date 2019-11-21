def solution(skill, skill_trees):
    answer = 0
    count=0
    list=[]
    for i in skill:
        list.append(i)
    print(list)
    x=len(skill)
    problem=False
    for skill_tree in skill_trees:
        for i in skill_tree:
            if i in list[1:x+1]:
                # print(list)
                problem=True
                break
            else:
                if i == skill[count]:
                    list.remove(list[0])
                    count+=1
                    problem=False
            count =0
        if problem==False:
            answer +=1
        
        print(problem)
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))