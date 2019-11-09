def solution(x, n):
    answer = []
    t=x*n+1
    for i in range(n):
        answer.append(x+i*x)
    return answer

x=4
n=3
print(solution(x,n))