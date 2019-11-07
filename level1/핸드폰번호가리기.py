def solution(s):
    answer = ''    
    t=len(s)
    t=t-4
    for a in range(0,t):
        answer+='*'
    answer+=s[t:]


    # print(''.join(answer.*)[0,t-4])
    return answer


s='01033334444'
print(solution(s))