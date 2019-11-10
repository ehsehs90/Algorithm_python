def solution(n):
    sum = 0
    
    for i in str(n):
        sum+=int(i)

    return sum

n=123
print(solution(n))