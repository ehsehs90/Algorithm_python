t_case_count = int(input()) #3
t_case_list =[]
arr = [1,2,4]

for i in range(4,11):
    # 현재 인덱스부터 앞으로 3자리까지의 인덱스 합 구하기
    arr.append(sum(arr[-3:]))
for i in range(t_case_count):
    t_case_list.append(int(input()))

for i in range(t_case_count):
    print(arr[t_case_list[i]-1])