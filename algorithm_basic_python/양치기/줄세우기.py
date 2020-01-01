t_case_count=int(input())
t_case_list=[]
dp =[1]*200
answer=0
for i in range(t_case_count):
    t_case_list.append(int(input()))


for i in range(t_case_count):

    for j in range(0,i+1):
        if(t_case_list[j]<t_case_list[i] and dp[j]+1>dp[i]):
            dp[i]=dp[j]+1


for i in range(t_case_count):
    if(answer<dp[i]):
        ans=dp[i]

print(t_case_count-ans)        