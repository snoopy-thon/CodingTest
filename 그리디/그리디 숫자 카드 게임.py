# 그리디 알고리즘
# 3-3. 숫자 카드 게임
# 내 풀이 : 각 행의 최소값을 구한 후, 그중에서 가장 큰 값 찾기

# 행의 개수 N과 열의 개수 M을 공백을 기준으로 입력받기
N, M = map(int,input().split())
data = []
Min = []
for i in range(N):
    data.append(list(map(int,input().split())))
# 각 행의 최소값 찾기
    Min.append(min(data[i]))

# 각 행의 최소값들 중 가장 큰 값 찾기
Max_Of_Min = max(Min)
print("정답 : ",Max_Of_Min)

# 책에 있는 풀이1 : 각 행의 최소값을 구한 후, 그중에서 가장 큰 값 찾기
# 내 풀이와 다른 점 : 핵심은 같으나, 나는 각 행의 최소값을 리스트에 모두 저장한 후 그중에서 가장 큰 값을 찾았는데
# 책에서는 이전 행의 최솟값과 현재 행의 최솟 값을 그때 그때 비교하여 가장 큰 수를 찾았다.

N, M = map(int,input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(N):
    data = list(map(int,input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result,min_value)
    
print(result)   # 최종 답안 출력

# 책에 있는 풀이2 : min()함수 안쓰고 2중 반복문 구조를 이용하는 답안 예시
N, M = map(int,input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int,input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value,a)
    result = max(result, min_value)
    
print(result)


