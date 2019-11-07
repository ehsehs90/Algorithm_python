def solution(n, arr1, arr2):
    answer = []
    
    for i,j in zip(arr1, arr2):
        # print(format((i|j),'b').rjust(n,'0'))
        a=format((i|j),'b')
        # print(a)
        s=a.replace('1','#')
        s=s.replace('0',' ')
        print(s)         
        answer.append(s)
    return answer



    # print(12|6)
    # for i,j in zip(arr1, arr2):
    #     # print(format(i,'b').rjust(n,'0'))
    #     # print(format(j,'b').rjust(n,'0'))
    #     # c = format(i,'b').rjust(n,'0')
    #     # d = format(j,'b').rjust(n,'0')
    #     k=i+j
    #     p=format(k,'b').rjust(n,'0')
    #     print(format(k,'b').rjust(n,'0'))
    #     pp=len(p)
    #     if(p==6):
        
    #     else:

     

    # for i in arr2:
    #     print(format(i,'b').rjust(n,'0'))    

n	=5
arr1=	[9, 20, 28, 18, 11]
arr2=	[30, 1, 21, 17, 28]
# 출력	["#####","# # #", "### #", "# ##", "#####"]

# format(42, 'b')
# '101010'

print(solution(n, arr1, arr2))