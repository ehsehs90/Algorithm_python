# 최대공약수 - 두 수 x,y에서 x의 약수이면서 y의 약수인 수 중 최대값
# 최대공약수를 구하는 간단한 방법
# 1에서 x와 y중 작은 값의 범위에서 공약수 (둘 모두 나머지가 0) 을 모두 구한 다음
# 이들 수의 최대값
# 유클리드호제법


def solution1(n, m):

    while m:
        n,m = m, n%m    
    return n

#최소공배수 : x,y의 공통된 배수 가운데 최소값
# 주어진 수인 x,y의 곱에서 x,y의 최대공약수를 나누어 준 것과 같다
def lcm(x,y):
    return x*y //solution1(x,y)
n=3
m=12


def solution(n, m):
    answer = []
    

    answer.append(solution1(n,m))
    answer.append(lcm(n,m))
    return answer

print(solution(n,m))