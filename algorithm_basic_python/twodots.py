# 4 칸 이동할 수 있으면 사이클이 존재한다.

input
dx= [0,0,1,-1]
dy = [1,-1,0,0]

n,m = map(int , input().split()) #n=3, m=4
a = [input() for _ in range(n)]
dist = [[0]*m for _ in range(n)]
check = [[False]*m for _ in range(n)]


# (x,y) 도착, 현재 cycle 은 color . cnt = 방문한 개수
def go (x,y,cnt, color):
    if check[x][y]:
        if cnt-dist[x][y] >=4:
            return True
        else:
            return False
    check[x][y] =True
    dist[x][y] = cnt
    for k in range(4):
        nx, ny = x +dx[k], y+dy[k]

        if 0 <= nx < n and 0 <= ny < m:

            if a[nx][ny] == color:
                if go(nx,ny,cnt+1,color):
                    return True

    return False


for i in range(n):
    for j in range(m):
        if check[i][j]:
            continue

        dist = [[0]*m for _ in range(n)]
        print(dist)
        ok = go(i,j,1,a[i][j])

        if ok:
            print('Yes')
            exit()
print('no')