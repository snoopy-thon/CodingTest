# 구현 알고리즘
# 4-3. 왕실의 나이트
# 내 풀이 : 문제푸는데 매우 오래걸림. 문제를 풀 때 데이터를 너무 규칙을 찾아서 풀려고 하지말기
# 그냥 간단한 데이터는 있는 그대로 나열하는 게 더 좋을지도 모름.
# 규칙성을 찾으려고 너무 오랜시간을 투자하기 보다는 일단 단순하게 써보고 그 다음 규칙을 발견하면 바꾸는게 나은듯.
'''
# 첫번째 나의 풀이(실패함)
# 현재 나이트가 위치한 좌표
now = input()
column = now[0]    # 열 : 알파벳
row = int(now[1]) # 행 : 숫자

# 나이트가 수평,수직으로 움직일 수 있는 경우
row_type = [[row-1,row+1],[row-2, row+2]]
column_type = [[ord(column)-2,ord(column)+2],[ord(column)-1,ord(column)+1]]

# 나이트가 이동할 수 있는 경우의 수 구하기
count = 0
for j in range(2):
    if row_type[1][j] > 0 and row_type[1][j] < 9 :
        if column_type[1][j] >= ord('a') and column_type[1][j] <= ord('h') :
            count += 1
    if column_type[0][j] >= ord('a') and column_type[0][j] <= ord('h') :
        if row_type[1][j] > 0 and row_type[1][j] < 9 :
            count += 1
                
print(count)    
'''
# 두번째 나의 풀이
# 현재 나이트가 위치한 좌표
now = input()
column = now[0]    # 열 : 알파벳
row = int(now[1]) # 행 : 숫자

# 나이트가 움직일 수 있는 방향
direction = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[1,-2]]
col = ord(column)

# 나이트가 이동할 수 있는 경우의 수 구하기
count = 0
for i in range(8):
    # 이동하고자 하는 위치 확인
    c = col + direction[i][0]
    r = row + direction[i][1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if r >= 1 and r <= 8 and c >= ord('a') and c <= ord('h'):
        count += 1
print(count)

# 책 풀이 : 두번째 나의 풀이와 비슷하여 생략.
