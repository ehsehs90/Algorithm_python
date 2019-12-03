def solution(people, limit):
    answer = 0
    people.sort()
    light=0
    length = len(people)
    print(length)
    heavy = length-1
    print(people)

    while(light<heavy):

        if(people[light]+people[heavy] <= limit):
            print(people[light])
            heavy-=1
            light+=1
            answer+=1
        else:
            heavy-=1

    return length-answer

    # 탐욕법
    

people = [70, 50, 80, 50]
limit = 100
print(solution(people,limit))

