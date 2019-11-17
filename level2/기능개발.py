def solution(progresses, speeds):
    answer = []
    while(len(progresses)):
        count=0
        bool  = False
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        while(len(progresses)!=0 and progresses[0]>100):
            bool= True
            del progresses[0]
            del speeds[0]
            count+=1
        if bool:
            answer.append(count)

    return answer

progresses=[93,30,55]
speeds=[1,30,5]
print(solution(progresses, speeds))