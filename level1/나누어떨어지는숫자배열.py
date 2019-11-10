def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if len(answer)==0:
        return [-1]    
    arr.sort()    
    return answer




arr=[5,9,7,10]
divisor=15
print(solution(arr, divisor))