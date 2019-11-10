def solution(d, budget):

    sum=0
    answer=0
    d.sort()
        # 1 2 3 4 5
    for i in d:    

        if sum + i <=budget:
            sum+= i
            answer += 1
        else:
            break
    return answer




d=[1,3,2,5,4]
budget=9
print(solution(d,budget))