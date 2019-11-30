def solution(n):
    answer = 0
    a, b= 1,0
    for i in range(n):
        a,b = b, a+b
        print(a)
        print(b)
    return b%1234567




n= 3
print(solution(n))