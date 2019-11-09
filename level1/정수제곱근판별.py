def solution(n):
    answer = 0

    x = int(n ** 0.5)
    print(x)
    y= int(pow(x,2))
    print(y)
    if(n!=y):
        return -1
    else:
        pass
    answer = pow(x+1,2)
    return answer


n = 3
print(solution(n))