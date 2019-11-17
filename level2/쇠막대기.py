def solution(arrangement):
    answer = 0
    stack=[]
    arrangement=arrangement.replace("()","L")
    for i in arrangement:
        if i =="(":
            stack.append(i)
            answer +=1               
                    
        elif i ==")":
            stack.pop()
            
        else:
            answer += len(stack)        
    return answer

arrangement="(()()((()()())))"
# arrangement="()(((()())(())()))(())"
print(solution(arrangement))