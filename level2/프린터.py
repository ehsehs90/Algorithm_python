def solution(priorities, location):
    pos=[]
    for i in range(len(priorities)):
        if i == location:
            pos.append(True)
            print('왜안대')
        else:
            pos.append(False)   # t/f mask만들기    
    count =0
    m=max(priorities)
    while True:
        if m > priorities[0]:
            priorities.append(priorities.pop(0))
            pos.append(pos.pop(0))
        else:
            count+=1
            priorities.pop(0)
            if pos.pop(0):
                return count

            m= max(priorities)

            
priorities = [2, 1, 3, 2]	
location = 2
print( solution(priorities, location))