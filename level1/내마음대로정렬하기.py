def solution(strings, n):
    a=sorted(strings ,reverse=False)
    answer=sorted(a, key=lambda x:x[n] )
    print(answer)
    
    return answer




strings=['abce', 'abcd', 'cdx']
# strings=["sun", "bed", "car"]
n=1
solution(strings, n)