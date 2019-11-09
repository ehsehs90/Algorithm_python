def solution(s):
    answer = ''

    list=[]
    list=s.split(' ')
    # print(list)
    for i in list:
        k=len(i)
        for j in range(k):
            if(j%2==0):
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer+=(' ')
   
        # p=len(i)
        # for q in range (p):
        #     if i[q%2==0]:
        #         print(i[q%2==0])
            
        #     if(q%2==0):
        #         print(str())

    return answer


s="try hello world"
print(solution(s))