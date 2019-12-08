import re
from collections import Counter

pattern = re.compile('[a-z][a-z]')

def preprocessing(content):
    result=[]
    for i in range(0, len(content)-1):
        two_letter = content[i:i+2]
        if pattern.search(two_letter):
            result.append(two_letter)
    print(result)
    return result

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    if str1 == str2:
        return 65536

    str1 = preprocessing(str1)
    str2 = preprocessing(str2)


    # collections.Counter 를 이용해서 중복되는 개수를 허용하는 자료형을 쓴다
    # 또한 collections.Counter 는 교집합(&), 합집합(I)를 제공한다.


    counter_1 = Counter(str1)
    counter_2 = Counter(str2)
    print('counter 자료형 이란?')
    print('데이터의 개수를 셀 때 사용')
    print(counter_1)
    print(counter_2)
    intersections = counter_1 & counter_2
    intersections = sum(list(intersections.values()))


    unions = counter_1 | counter_2
    unions = sum(list(unions.values()))
    return int(intersections/unions* 65536)


    return answer

str1 = "FRANCE"
str2 = "french"
print(solution(str1,str2))