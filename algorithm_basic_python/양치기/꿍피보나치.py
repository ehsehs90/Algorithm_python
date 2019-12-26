t_case_count=int(input())
t_case_list=[]


for i in range (t_case_count):
    t_case_list.append(int(input()))

kkung_fibonacci=[1,1,2,4]


for i in range (64):
    kkung_fibonacci.append(kkung_fibonacci[-1]+kkung_fibonacci[-2]+kkung_fibonacci[-3]+kkung_fibonacci[-4])

for i in range(t_case_count):
    print(kkung_fibonacci[t_case_list[i]])