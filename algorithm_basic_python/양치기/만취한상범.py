t_case_count =int(input())
t_case_list=[]

for i in range (t_case_count):
    t_case_list.append(int(input()))

for n in t_case_list:
    answer =0
    for i in range(1, int(n)+1):
        if i**2<=n:
            answer +=1
        if i**2 >n:
            break
        
    print(answer)
