import sys

N,K = map(int, sys.stdin.readline().split())
coin=[]

for i in range (N):
    coin.append(int(sys.stdin.readline()))

target=K
#0 초기화 list
need=[0 for _ in range(N)]
idx = N-1
last_idx=N-1
lastlast_idx=N-1

while target !=0:
    # need list(갯수) 완성시키면
    # if idx<0:
    #     print('@@@@')
    #     target -= coin[last_idx] *need[last_idx]
    #     need[last_idx]=0
    #     target+=coin[lastlast_idx]
    #     need[lastlast_idx]-=1
    #     idx=lastlast_idx-1
    #     continue
    

    if target<coin[idx]:
        idx-=1
        continue

    need[idx]= target//coin[idx]
    print(need[idx])
    target%= coin[idx]
    print(target)
    lastlast_idx=last_idx
    last_idx=idx

print(sum(need))
