def solution(a, b):
    answer = ''
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    

    t=sum(month[:a-1])+b-2
    answer=day[t%7]
    # print(day[t%7])
    # print=(answer)
 
    return answer


# def PrintDay():
#     return


a=5
b=24
# a='qwer'

print(solution(a,b))