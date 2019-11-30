def solution(n):
    answer = 0
    a, b= 1,0
    for i in range(n):
        a,b = b, a+b
    return b




n= 3
print(solution(n))