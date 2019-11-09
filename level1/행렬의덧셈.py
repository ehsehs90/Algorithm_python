def solution(arr1, arr2):
    answer = []

    for i,j in zip(arr1,arr2):
        answer2 = []
        for k,l in zip(i,j):
            answer2.append (k+l)
            print(answer2)
        answer.append(answer2)
        # print(answer)
    return answer




arr1=[[1,2],[2,3]]
arr2=[[3,4],[5,6]]


print(solution(arr1,arr2))