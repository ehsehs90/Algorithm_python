def solution(s):
    
    y = 0
    p =0
    t=s.lower()

    for i in t:        
        if i=='p'or i=='P':
            y+=1            
        elif i=='Y'or i=='y':
            p+=1

    if y==p:
        return True
    else:
        return False       

s='pPoooyY'
print(solution(s))