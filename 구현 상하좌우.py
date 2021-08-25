# 구현 알고리즘
# 4-1. 상하좌우
# 내 풀이 :

# N을 입력받기
N = int(input())
plan = input().split()
x,y = 1,1

# 입력받은 이동 계획에 따라 x,y좌표 구하기
for i in plan:
    if y < N and i == 'R':
        y += 1
    if y > 1 and i == 'L':
        y -= 1
    if x > 1 and i == 'U':
        x -= 1
    if x < N and i == 'D':
        x += 1

    
print(x,y)    

# 책 풀이
n = int(input())
x,y = 1,1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    # 이동 수행
    x, y = nx, ny
    
print(x, y)
