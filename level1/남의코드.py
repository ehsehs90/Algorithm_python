
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''

    min = []
    result = []
    for i in strings:
        min.append(i[n])
        sorted_min = sorted(min)
        print(sorted_min)

    while len(result) != len(strings):
        for j in range(0, len(strings)):
            for k in range(0, len(strings)):
                if sorted_min[j] in strings[k][n]:
                    index = k
                    result.append(strings[index])
                    print(result.append(strings[index]))
                    continue

    return result
strings=['abce', 'abcd', 'cdx']
# strings=["sun", "bed", "car"]
n=1
strange_sort(strings, n)