def solution(x, n):
    answer = []

    for i in range(n):
        answer.append(x+i*x)
    return answer

x=4
n=3
print(solution(x,n))