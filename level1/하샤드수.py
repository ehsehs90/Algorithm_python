def solution(arr):
    answer = True
    
    a=0
    for i in arr:
        a+=int(i)
    if int(arr)%a==0:
        return "true"
    else:
        return "false"

arr =str(10)
print(solution(arr))