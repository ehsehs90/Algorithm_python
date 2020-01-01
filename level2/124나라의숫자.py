def solution(n):
    answer = ''
    mok=1
    list = [1,2,4]

    while mok!=0:
        mok = n//3 #1
        nam = n%3  #2
        if nam==0:
            mok -= 1
        n=  mok
        answer = str(list[nam-1]) + answer

    return answer 

n=5
print(solution(n))
print('@')