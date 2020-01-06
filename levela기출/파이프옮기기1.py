def dfs(x,y,z):
    global k
    if x==n -1 and y ==n -1 : k+=1
    if z ==0 or z ==1 : #가로로 움직이는경우의수
        if y+1 <n:
            if D[x][y+1] ==0:
                dfs(x,y+1,0)
    if z==0 or z==1 or z==2: # 대각선으로 움직일 수 있는 경우의수
        if x+1 <n and y+1 <n: 
            if D[x+1][y] == D[x][y+1] == D[x+1][y+1] ==0:
                dfs(x+1, y+1,1)
    if z==1 or z==2:
        if x+1 <n:
            if D[x+1][y] ==0:
                dfs(x+1,y,2)


n = int(input())
D = [[*map(int, input().split())]for _ in range(n)]
print(D)
k=0
dfs(0,1,0) #(0.1)
print(k)