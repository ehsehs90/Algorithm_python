def solution(citations):  
    harr=[]
    
    harr= sorted(citations, reverse=True)
    # if 0 not in harr:
    #     return len(harr)
    print(harr)
    for i,x in enumerate(harr):
        if x <= i:
            return i
    
    
    return 3

citations = [3,0,6,1,5]
print(solution(citations))