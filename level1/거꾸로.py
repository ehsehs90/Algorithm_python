def solution(s):
    # answers
    #스트링 거꾸로 출력하기
    # answer=s[::-1]
    # s=''.join(reversed(s))
    # print(s)
    return ''.join(sorted(s, reverse=True))

s="Zbcdefg"
print(solution(s))