def solution(name):
    answer = 0
    name_len = len(name)
    print(name_len)
    init="A"*name_len
    print(init)
    chk=[]
    for i in range(name_len):
        if ord(name[i])==65:
            pass
        else:
            tmp=ord(name[i])-65
            chk.append(i)
            if tmp>13:
                answer+=26-tmp
            else:
                answer+=tmp
        ind=0

        while chk!=[]:  
            tmp1=min(abs(chk[0]-ind),name_len-abs(chk[0]-ind))
            tmp2=min(abs(chk[-1]-ind),name_len-abs(chk[-1]-ind))

            min_chk=min(tmp1,tmp2)
            print("tmp1:{}\ttmp2:{}".format(tmp1,tmp2))
            if tmp1>tmp2:               
                ind=chk.pop()  
                answer+=tmp2
            else :               
                ind=chk.pop(0)
                answer+=tmp1
            print("ind:{}\tchk:{}".format(ind,chk))
    return answer



name="JEROEN"
print(solution(name))