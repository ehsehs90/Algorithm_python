
def solution(record):
    idDict = dict()
    answer = []
    logList=[]
    for e in record:
        dataList = e.split(" ")
        if dataList[0] == "Enter":
            idDict[dataList[1]] = dataList[2]
            print(dataList[2])
            logList.append([dataList[1], "님이 들어왔습니다."])
        elif dataList[0] == "Leave":
            logList.append([dataList[1], "님이 나갔습니다."])
        elif dataList[0] == "Change":
            idDict[dataList[1]] = dataList[2]
            
    print(logList)
    for log in logList:
        print(log)
        # print(log[1]+ '@')
        answer.append(idDict[log[0]]+ log[1])
    return answer


record = ["Enter uid1234 Muzi", 
"Enter uid4567 Prodo",
"Leave uid1234",
"Enter uid1234 Prodo",
"Change uid4567 Ryan"]
print(solution(record))