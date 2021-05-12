n, m = map(int, input().split())

# visited
check_visit = [[0]*m for _ in range(n)]

x, y, direction = map(int, input().split())
array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

check_visit[x][y] = 1
result = 1

# N, E, S, WEST
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


turn_time = 0

for i in range(n):
    for j in range(m):
        check_visit[i][j] += array[i][j]

while True:
    turn_left()

    if turn_time == 4:
        nx = x-dx[direction]
        ny = y-dx[direction]

        if check_visit[nx][ny] != 0:
            break
        else:
            turn_time = 0
            continue
    # CORE PART OF THIS CODES!
    nx = x+dx[direction]
    ny = y+dy[direction]
    # Range Check!
    if nx < 0 or ny < 0 or nx > n or ny > m:
        turn_time += 1
        continue

    # not visited
    if check_visit[nx][ny] == 0:
        x, y = nx, ny
        check_visit[x][y] = 1
        turn_time = 0
        result += 1
        continue

    else:
        turn_time += 1
        continue

print(result)
