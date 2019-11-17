def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
# list[1](의상의종류) 을 기준(key값)으로 분리
        if i[1] in dic:
            dic[i[1]].append(i[0])
        else:
            dic[i[1]] = [i[0]]
        # print(list)
# for 문을 통해 딕셔너리를 for문을 돌리면 key값이 할당된다.
# 순서는 임의적이다. 같은 순서를 보장할 수 없다.
    for k in dic:
        answer *= len(dic[k])+1
#의상종류 중 반드시 하나는 선택해야하므로, 아무것도 선택하지 않을 확률을 빼야한다.

    return answer-1

# 서로 다른 조합의 수 return 하는 solution 함수
clothes=[['yellow_hat', 'headgear'], #1
['blue_sunglasses', 'eyewear'], 
['green_turban', 'headgear']] #2

print(solution(clothes))