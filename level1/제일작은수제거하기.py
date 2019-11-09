def solution(arr):
    answer = []
    if len(arr)>1:


        arr.remove(min(arr))
    else:
        return -1
    return arr

arr=[4,3,2,1]
# arr=[10]
print(solution(arr))