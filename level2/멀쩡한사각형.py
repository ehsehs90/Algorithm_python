import math
def solution(w,h):

    perfect_rectangular = 0
    perfect_rectangular = w*h


    gcd=math.gcd(w,h)
    answer = perfect_rectangular - ( w + h - gcd) 


    return answer


w=8
h=12
gcd=math.gcd(w,h)
print(gcd)
print(solution(w,h))