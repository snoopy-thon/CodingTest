# 그리디 알고리즘
# 3-2. 큰 수의 법칙
# 내 풀이 : 가장 큰 수가 한개일 때와 여러개일 때의 경우로 나눠서 풀었음.
N, M, K = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
Max = max(num)
Max_count = num.count(Max)
ind = num.index(Max)
new = num[:ind]
new_Max = max(new)
result = 0
print("정렬된 리스트 : ",num)
print("Max : ",Max)
print("Max_count : ",Max_count)
print("두번째로 큰 수 : ",new_Max)
if Max_count > 1:
    result = Max * K * (M // K) + Max * (M % K)
else:
    result = (Max * K + new_Max)*(M // (K+1)) + Max * (M % (K+1))

print(result)

# 책에 있는 풀이 : 굳이 나처럼 두가지 케이스로 나누지 않고 일반화해서 품.
# 그 대신 가장 큰 수가 더해지는 횟수와 두 번째로 큰 수가 더해지는 횟수를 나누어서 계산함.
# N,M,K를 공백으로 구분하여 입력받기
N, M, K = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
num = list(map(int, input().split()))

num.sort()  # 입력받은 수 정렬
first = num[N-1]    # 가장 큰 수
second = num[N-2]   # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = K * (M // (K+1)) + M % (K+1)

result = 0
result += first * count     # 가장 큰 수 더하기
result += second * (M - count)  # 두 번째로 큰 수 더하기
print(result)   # 최종 답안 출력
