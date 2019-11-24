def solution(heights):
    answer = [0] * len(heights)
    p=len(heights)
    # print(len(heights))
    while( p > 0 ):

        right = heights.pop()
        for idx in range(p-2,0,-1):
            if heights[idx]>right:
                print(heights[idx])
                answer[len(heights)] = idx+1
                
                break
        p-=1
    return answer


# heights=[3,9,9,3,5,7,2]
heights =[6,9,5,7,4]
print(solution(heights))