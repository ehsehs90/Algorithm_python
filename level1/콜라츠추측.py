def solution(num):

    result=0
    while(num!=0):
        if(result==500):
            return -1
        if (num==1):

            return result
        if(num%2==0):
            num=num/2
        
        else:
            num=num*3+1
        result+=1
    
    
    return result


n=626331
print(solution(n))