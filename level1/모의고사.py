from itertools import cycle

def solution(answers):
    # print(answers)
    winner=[]
    arr1 =[1,2,3,4,5]
    arr2 =[2,1,2,3,2,4,2,5]
    arr3 =[3,3,1,1,2,2,4,4,5,5]
    count=[0,0,0]

    for i, j, k, answer in zip(cycle(arr1), cycle(arr2), cycle(arr3), answers):
        if i == answer: count[0]+=1
        if j == answer: count[1]+=1 
        if k == answer: count[2]+=1 
    
    for i, score in enumerate(count):
        if score == max(count):
            winner.append(i+1)

    
    return winner








answers=[1,2,3,4,5]

print(solution(answers))