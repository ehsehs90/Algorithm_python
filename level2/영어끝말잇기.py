def solution(n, words):
    answer = [0,0]
    past = []
    past.append(words[0])
    words.remove(words[0])
    count = 0
    problem =False

    for word in words:
        count +=1
        if word in past:
            problem=True
            break
        else:
            past.append(word)
            if past[-2][-1] == past[-1][0]:
                print('여길들어온다고?')
                pass
            else:
                problem=True
                break
    print(problem)
    if not problem:
        return answer
    else:
        answer[1],answer[0]=divmod(count,n)
        answer[0]+=1
        answer[1]+=1
    return answer


# n = 5
# words= ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]

words = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']
n = 3
print(solution(n,words))